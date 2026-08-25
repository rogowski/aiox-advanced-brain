#!/usr/bin/env python3
"""Compute the aula 21b scorecard. Do not invent arithmetic in the model."""

from __future__ import annotations

import json
import sys
from pathlib import Path

Q_KEYS = [f"q{i}" for i in range(1, 10)]
T_KEYS = [f"t{i}" for i in range(1, 5)]
B_KEYS = [f"b{i}" for i in range(1, 5)]
ROUND_KEYS = ("id", "modelo", "runtime", "started_at", "capability")
ALLOWED_CAPABILITY = {"alto", "override"}

BANDS = (
    (3, "soldado"),
    (6, "separação parcial"),
    (9, "troca operacional"),
)

LADDER = (
    "acoplamento físico",
    "adapter",
    "contrato de capability",
    "eval gate",
    "substituição operacional",
)


def _round(card: dict) -> dict:
    raw = card.get("round")
    if not isinstance(raw, dict):
        raise ValueError("scorecard.round é obrigatório (id, modelo, runtime, started_at, capability)")
    missing = [key for key in ROUND_KEYS if not str(raw.get(key) or "").strip()]
    if missing:
        raise ValueError(f"scorecard.round falta: {', '.join(missing)}")
    capability = str(raw["capability"]).strip().lower()
    if capability not in ALLOWED_CAPABILITY:
        raise ValueError("scorecard.round.capability deve ser alto ou override")
    blocked = str(raw.get("blocked_class") or "").strip().lower()
    if capability == "override" and blocked not in {"leve", "medio", "desconhecido"}:
        raise ValueError("override exige round.blocked_class: leve|medio|desconhecido")
    return {
        "id": str(raw["id"]).strip(),
        "modelo": str(raw["modelo"]).strip(),
        "runtime": str(raw["runtime"]).strip(),
        "started_at": str(raw["started_at"]).strip(),
        "harness": str(raw.get("harness") or "").strip(),
        "capability": capability,
        "blocked_class": blocked,
    }


def _as_bool(value, key: str) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, dict):
        if "yes" in value:
            result = value["yes"]
            if not isinstance(result, bool):
                raise ValueError(f"{key}.yes precisa ser bool")
            return result
        if "value" in value:
            result = value["value"]
            if not isinstance(result, bool):
                raise ValueError(f"{key}.value precisa ser bool")
            return result
    raise ValueError(f"{key} precisa ser bool ou {{yes: bool}}")


def _band(total: int) -> str:
    for limit, name in BANDS:
        if total <= limit:
            return name
    return "troca operacional"


def _modelo_level(answers: dict[str, bool]) -> int:
    if not answers["q1"]:
        return 0
    if not answers["q2"]:
        return 1
    if not answers["q6"]:
        return 2
    if not answers["q7"]:
        return 3
    return 4


def score(card: dict) -> dict:
    answers = {key: _as_bool(card["answers"][key], f"answers.{key}") for key in Q_KEYS}
    thickness = {key: _as_bool(card["thickness"][key], f"thickness.{key}") for key in T_KEYS}
    brain = {key: _as_bool(card["brain"][key], f"brain.{key}") for key in B_KEYS}

    total = sum(answers.values())
    modelo = _modelo_level(answers)
    harness = sum(thickness.values())
    brain_score = sum(brain.values())
    q9 = answers["q9"]

    return {
        "repo": card.get("repo", ""),
        "round": _round(card),
        "diagnostico": {
            "total": total,
            "max": 9,
            "banda": _band(total),
            "respostas": answers,
        },
        "pilares": {
            "modelo": {"score": modelo, "max": 4, "degrau": LADDER[modelo]},
            "harness": {
                "score": harness,
                "max": 4,
                "operacional_bloqueado": harness == 4 and not q9,
            },
            "brain": {"score": brain_score, "max": 4},
        },
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("uso: score.py <scorecard.json>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    card = json.loads(path.read_text(encoding="utf-8"))
    result = score(card)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
