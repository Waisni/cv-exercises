@echo "Running ResNet-18 on CIFAR-10 with frost corruption severity 2"
@echo "Number of Batch Size: 1"
@python run_resnet.py --data_dir ..\data\ --corruption "frost" --severity 2 --apply_bn --batch_size 1 --num_bn_updates 50 | findstr "Loss Accuracy"

@echo "Number of Batch Size: 4"
@python run_resnet.py --data_dir ..\data\ --corruption "frost" --severity 2 --apply_bn --batch_size 4 --num_bn_updates 50 | findstr "Loss Accuracy"

@echo "Number of Batch Size: 16"
@python run_resnet.py --data_dir ..\data\ --corruption "frost" --severity 2 --apply_bn --batch_size 16 --num_bn_updates 50 | findstr "Loss Accuracy"

@echo "Number of Batch Size: 64"
@python run_resnet.py --data_dir ..\data\ --corruption "frost" --severity 2 --apply_bn --batch_size 64 --num_bn_updates 50 | findstr "Loss Accuracy"
