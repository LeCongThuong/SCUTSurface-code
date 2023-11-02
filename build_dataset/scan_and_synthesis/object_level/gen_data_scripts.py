import subprocess

base_directory = "/mnt/hdd/thuonglc/mocban/woodblock-character-evaluation/data/normalized"
num_worker = 1

commands = [
    # f'./Blensor-x64.AppImage --background -P camera_rotate_scan_batch.py blensor_scan_list.txt',
    # f"python estimate_normal_batch.py --In_Nonuniform_Dir /mnt/hdd/thuonglc/mocban/woodblock-character-evaluation/data/normalized/Nonuniform --Out_Nonuniform_Normal_Dir /mnt/hdd/thuonglc/mocban/woodblock-character-evaluation/data/normalized/Nonuniform_Normal --In_Noise_Dir /mnt/hdd/thuonglc/mocban/woodblock-character-evaluation/data/normalized/Noise --Out_Noise_Normal_Dir /mnt/hdd/thuonglc/mocban/woodblock-character-evaluation/data/normalized/Noise_Normal --num_worker 1",
    # f"python synthetic_dataset_batch.py --Base_dir_in {base_directory} -w Nonuniform --num_worker {num_worker}",
    f"python synthetic_dataset_batch.py --Base_dir_in {base_directory} -w Noise -sl 1 -an 0.001 --num_worker {num_worker}",
    # f"python synthetic_dataset_batch.py --Base_dir_in {base_directory} -w Noise -sl 2 -an 0.003 --num_worker {num_worker}",
    # f"python synthetic_dataset_batch.py --Base_dir_in {base_directory} -w Noise -sl 3 -an 0.006 --num_worker {num_worker}",
    # f"python synthetic_dataset_batch.py --Base_dir_in {base_directory} -w Outlier -sl 1 -on 0.0001 -oi 0.1 --num_worker {num_worker}",
    # f"python synthetic_dataset_batch.py --Base_dir_in {base_directory} -w Outlier -sl 2 -on 0.0003 -oi 0.1 --num_worker {num_worker}",
    # f"python synthetic_dataset_batch.py --Base_dir_in {base_directory} -w Outlier -sl 3 -on 0.0006 -oi 0.1 --num_worker {num_worker}",
    # f"python synthetic_dataset_batch.py --Base_dir_in {base_directory} -w MissingData -sl 1 --num_worker {num_worker}",
    # f"python synthetic_dataset_batch.py --Base_dir_in {base_directory} -w MissingData -sl 2 --num_worker {num_worker}",
    # f"python synthetic_dataset_batch.py --Base_dir_in {base_directory} -w MissingData -sl 3 --num_worker {num_worker}",
    # f"python synthetic_dataset_batch.py --Base_dir_in {base_directory} -w Misalignment -sl 1 -mi 0.005 -mma 0.5 --num_worker {num_worker}",
    # f"python synthetic_dataset_batch.py --Base_dir_in {base_directory} -w Misalignment -sl 2 -mi 0.01 -mma 1 --num_worker {num_worker}",
    # f"python synthetic_dataset_batch.py --Base_dir_in {base_directory} -w Misalignment -sl 3 -mi 0.02 -mma 2 --num_worker {num_worker}"
]

for command in commands:
    subprocess.run(command, shell=True)
