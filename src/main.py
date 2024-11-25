"""Module to show examples about hydra."""

import pandas as pd 
import hydra
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="hydra")


@hydra.main(config_path="config", config_name="config_main", version_base="1.1")
def main_func(cfg) -> None:
    """Example main function."""
    print(cfg)

if __name__ == "__main__":
    main_func()