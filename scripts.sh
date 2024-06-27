python main_directory.py \
    -t assets/weights/mbf_large_v3.onnx \
    -a assets/weights/attack_idiap_v3.onnx \
    -i assets/images \
    -o assets/outputs/3v3

python main_single.py \
    -t assets/weights/mbf_large_v1.onnx \
    -a assets/weights/attack_idiap_v1.onnx \
    -i assets/images/0.jpg \
    -o assets/outputs \
    -v