while [ 1 ]
do
    nvidia-smi
    gpu_index=$(nvidia-smi --query-gpu=index,memory.free --format=csv,noheader,nounits | \
                awk -F',' '{print $2, $1}' | \
                sort -nr | \
                head -n 1 | \
                awk '{print $2}')
    export CUDA_VISIBLE_DEVICES="$gpu_index"
    echo "Selected GPU index with max memory.free: $gpu_index"

    python3 main.py && break
    
    sleep 300
done