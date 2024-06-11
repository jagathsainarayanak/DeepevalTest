from Benchmarks.MMLU_Dataset import MMLU_Data
from Benchmarks.HellaSwag_Dataset import Hellaswag_data
from Benchmarks.TruthfulQA_Dataset import TruthfulQA_data
from Benchmarks.GSM8k_dataset import GSM8k_Data
import argparse

def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--benchmark", default='mmlu',type = str)
    args = parser.parse_args()
  
    if args.benchmark=='mmlu':
        MMLU_Data().run_mmlu()
    elif args.benchmark=='hellaswag':
        Hellaswag_data().run_Hellaswag()
    elif args.benchmark=='truthfulQA':
        TruthfulQA_data().run_TruthfulQA()
    elif args.benchmark=='gsm':
        GSM8k_Data().run_gsm()

if __name__=="__main__": 
    main()