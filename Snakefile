import os
project_dir=os.path.abspath(os.curdir) + '\..\..'
os.chdir(project_dir)

from pathlib import Path

rule all:
    input:
        Path("reports/res_result.csv"),
        Path("reports/test_prepared.csv"),
        Path("reports/train_prepared.csv"),
        Path("reports/test_processed.csv"),
        Path("reports/train_processed.csv")

rule prepare_data:
    output:
        Path("test"),
        Path("train"),
        Path("passenger_id")
    params:
        cli=Path("workflow/scripts/cli.py"),
    shell:
        "python {params.cli} prepare-data {output}"

rule create_features:
    output:
        Path("test"),
        Path("train")
    params:
        cli=Path("workflow/scripts/cli.py"),
    shell:
        "python {params.cli} create-features {output}"

rule print_info:
    input:
        Path("data/train.csv")
    output:
        Path("test"),
        Path("train")
    params:
        cli=Path("workflow/scripts/cli.py"),
    shell:
        "python {params.cli} print-info {input} {output}"

rule logReg_result:
    output:
        Path("result"),
    params:
        cli=Path("workflow/scripts/cli.py"),
    shell:
        "python {params.cli} logreg-result {output}"