# -*- coding: utf-8 -*-
"""Sinh tệp điểm so khớp tổng hợp cho bài thực hành TH01.

Tệp kết quả scores_th01.csv có ba cột: system, pair_type, score.
- system A: điểm tương đồng (similarity) trong [0, 1], hai phân bố cân đối.
- system B: điểm tương đồng, cặp khác người có "đuôi nặng" (3% cặp khó).
- system C: điểm khoảng cách (distance), càng nhỏ càng giống nhau.

Dữ liệu hoàn toàn tổng hợp bằng bộ sinh số ngẫu nhiên có hạt giống cố định,
không xuất phát từ bất kỳ người thật nào. Chạy lại sẽ cho đúng tệp cũ.

Cách chạy: python make_scores.py
"""
import csv
import sys
from pathlib import Path

import numpy as np

SEED = 4211          # mã học phần, dùng làm hạt giống để ai chạy cũng ra cùng dữ liệu
N_GENUINE = 1000     # số cặp cùng người cho mỗi hệ thống
N_IMPOSTOR = 10000   # số cặp khác người cho mỗi hệ thống


def make_system_a(rng):
    gen = rng.beta(9.0, 3.0, N_GENUINE)
    imp = rng.beta(3.0, 9.0, N_IMPOSTOR)
    return gen, imp


def make_system_b(rng):
    gen = np.clip(rng.normal(0.66, 0.09, N_GENUINE), 0.0, 1.0)
    n_hard = int(round(0.03 * N_IMPOSTOR))
    imp_easy = rng.normal(0.28, 0.06, N_IMPOSTOR - n_hard)
    imp_hard = rng.normal(0.58, 0.08, n_hard)
    imp = np.clip(np.concatenate([imp_easy, imp_hard]), 0.0, 1.0)
    rng.shuffle(imp)
    return gen, imp


def make_system_c(rng):
    # khoảng cách: cặp cùng người có khoảng cách nhỏ
    gen = rng.gamma(shape=4.0, scale=0.08, size=N_GENUINE)
    imp = rng.normal(1.0, 0.15, N_IMPOSTOR)
    return np.clip(gen, 0.0, 2.0), np.clip(imp, 0.0, 2.0)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    rng = np.random.default_rng(SEED)
    rows = []
    for name, maker in [("A", make_system_a), ("B", make_system_b), ("C", make_system_c)]:
        gen, imp = maker(rng)
        rows += [(name, "genuine", f"{s:.4f}") for s in gen]
        rows += [(name, "impostor", f"{s:.4f}") for s in imp]
    out = Path(__file__).with_name("scores_th01.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["system", "pair_type", "score"])
        writer.writerows(rows)
    print(f"Đã ghi {len(rows)} dòng vào {out.name}")


if __name__ == "__main__":
    main()
