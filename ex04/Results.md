# Results

## Clean eval

Validation complete. Loss 0.937145 accuracy 76.29%

## Evaluate

Validation of defucus blur severety 1 Loss 1.860975 accuracy 55.79%
Validation of defocus_blur severity 2 Loss 2.305511 accuracy 47.08%
Validation of defocus_blur severity 3 complete. Loss 3.285967 accuracy 30.99%

Validation of glass_blur severity 1 complete. Loss 1.833410 accuracy 56.17%
Validation of glass_blur severity 2 complete. Loss 2.545328 accuracy 43.15%
Validation of glass_blur severity 3 complete. Loss 4.153072 accuracy 20.59%

Validation of motion_blur severity 1 complete. Loss 1.625862 accuracy 61.42%
Validation of motion_blur severity 2 complete. Loss 2.384517 accuracy 48.01%
Validation of motion_blur severity 3 complete. Loss 3.657122 accuracy 29.68%

Validation of zoom_blur severity 1 complete. Loss 2.453933 accuracy 48.41%
Validation of zoom_blur severity 2 complete. Loss 3.249248 accuracy 38.25%
Validation of zoom_blur severity 3 complete. Loss 3.868047 accuracy 30.66%

Validation of snow severity 1 complete. Loss 1.994411 accuracy 53.77%
Validation of snow severity 2 complete. Loss 3.805678 accuracy 27.27%
Validation of snow severity 3 complete. Loss 3.575052 accuracy 31.82%

Validation of frost severity 1 complete. Loss 1.699419 accuracy 59.44%
Validation of frost severity 2 complete. Loss 2.883014 accuracy 40.63%
Validation of frost severity 3 complete. Loss 3.890660 accuracy 27.21%

Validation of fog severity 1 complete. Loss 1.761400 accuracy 57.75%
Validation of fog severity 2 complete. Loss 2.223613 accuracy 48.99%
Validation of fog severity 3 complete. Loss 2.965221 accuracy 37.83%

Validation of brightness severity 1 complete. Loss 1.011865 accuracy 73.60%
Validation of brightness severity 2 complete. Loss 1.093004 accuracy 71.76%
Validation of brightness severity 3 complete. Loss 1.241478 accuracy 68.25%


{'brightness': [73.59673566878982, 71.75557324840764, 68.25238853503186],
 'defocus_blur': [55.792197452229296, 47.083996815286625, 30.99124203821656],
 'fog': [57.75278662420382, 48.99482484076433, 37.82842356687898],
 'frost': [59.44466560509554, 40.634952229299365, 27.209394904458602],
 'glass_blur': [56.17038216560509, 43.152866242038215, 20.591162420382165],
 'motion_blur': [61.415207006369435, 48.009554140127385, 29.677547770700635],
 'snow': [53.77189490445859, 27.269108280254777, 31.817277070063692],
 'zoom_blur': [48.40764331210191, 38.24641719745223, 30.662818471337577]}

## With apply_bn

Without:
Validation of frost severity 2 complete. Loss 2.883014 accuracy 40.63%
With:
Validation complete. Loss 2.431692 accuracy 48.43%

## Number of bn updates

"Number of BN updates: 1"
Validation complete. Loss 2.790674 accuracy 41.91%

"Number of BN updates: 5"
Validation complete. Loss 2.542053 accuracy 46.51%

"Number of BN updates: 10"
Validation complete. Loss 2.436787 accuracy 48.30%

"Number of BN updates: 20"
Validation complete. Loss 2.530079 accuracy 47.83%

"Number of BN updates: 50"
Validation complete. Loss 2.698212 accuracy 45.91%

"Number of BN updates: 100"
Validation complete. Loss 2.679301 accuracy 46.26%

## Number of Batch size

"Running ResNet-18 on CIFAR-10 with frost corruption severity 2"
"Number of Batch Size: 1"
Validation complete. Loss 4.430497 accuracy 28.39%
"Number of Batch Size: 4"
Validation complete. Loss 3.177386 accuracy 40.84%
"Number of Batch Size: 16"
Validation complete. Loss 2.759930 accuracy 44.71%
"Number of Batch Size: 64"
Validation complete. Loss 2.684843 accuracy 45.95%
