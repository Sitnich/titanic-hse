import os
project_dir=os.path.abspath(os.curdir)
os.chdir(project_dir)

from pathlib import Path

rule all:
    input:
        Path("reports/res_result.csv"),
rule prepare_data:
    output:
        Path("reports/train_prepared.csv"),
        Path("reports/test_prepared.csv"),
        Path("reports/passenger_id.csv")
    params:
        cli=Path("workflow/scripts/cli.py")
    shell:
        "python3 {params.cli} prepare-data {output}"

rule create_features:
    input:
        Path("reports/train_prepared.csv"),
        Path("reports/test_prepared.csv")
    output:
        Path("reports/train_processed.csv"),
        Path("reports/test_processed.csv")
    params:
        cli=Path("workflow/scripts/cli.py"),
    shell:
        "python3 {params.cli} create-features {output}"

rule print_info_train:
    input:
        Path("data/train.csv")
    output:
        Path("reports/train_info.csv")
    params:
        cli=Path("workflow/scripts/cli.py"),
    shell:
        "python3 {params.cli} print-info {input} {output}"

rule logReg_result:
    input:
        Path("reports/train_processed.csv"),
        Path("reports/test_processed.csv"),
        Path("reports/passenger_id.csv")
    output:
        Path("reports/res_result.csv")
    params:
        cli=Path("workflow/scripts/cli.py"),
    shell:
        "python3 {params.cli} logreg-result {output}"
