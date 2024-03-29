import argparse

def get_train_test_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch-size', type=int, default=16)
    parser.add_argument('--num-epochs', type=int, default=3)
    parser.add_argument('--lr', type=float, default=3e-5)
    parser.add_argument('--num-visuals', type=int, default=10)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--save-dir', type=str, default='save/')
    parser.add_argument('--train', action='store_true')
    parser.add_argument('--eval', action='store_true')
    parser.add_argument('--train-datasets', type=str, default='squad,nat_questions,newsqa')
    parser.add_argument('--run-name', type=str, default='multitask_distilbert')
    parser.add_argument('--recompute-features', action='store_true')
    parser.add_argument('--train-dir', type=str, default='datasets/indomain_train')
    parser.add_argument('--val-dir', type=str, default='datasets/indomain_val')
    parser.add_argument('--eval-dir', type=str, default='datasets/oodomain_test')
    parser.add_argument('--eval-datasets', type=str, default='race,relation_extraction,duorc')
    parser.add_argument('--do-train', action='store_true')
    parser.add_argument('--do-eval', action='store_true')
    parser.add_argument('--sub-file', type=str, default='')
    parser.add_argument('--visualize-predictions', action='store_true')
    parser.add_argument('--eval-every', type=int, default=5000)

    parser.add_argument('--meta-train-dir', type=str, default="datasets/indomain_train/squad")
    parser.add_argument('--meta-val-dir', type=str, default= "datasets/indomain_val/squad")
    parser.add_argument('--save-meta-dir', type=str, default='save/meta_train_models/checkpoint')
    parser.add_argument('--alpha', type=float, default=.02)
    parser.add_argument('--beta', type=float, default=.1)
    parser.add_argument('--num-iteration', type=int, default=10)
    parser.add_argument('--batch', type=int, default=16)
    parser.add_argument('--epoch-num', type=int, default=3)

    
    
    
    args = parser.parse_args()
    return args