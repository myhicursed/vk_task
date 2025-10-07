import json
import matplotlib.pyplot as plt

def load_vmaf_mean(file_path):                                  #читаем среднее значение vmaf
    with open(file_path, "r") as f:
        data = json.load(f)
    return data["pooled_metrics"]["vmaf"]["mean"]

def prepare_data(files):                                        #наполянем два списка, для построения графика в дальнейшем
    bitrates = []
    vmafs = []
    for f, br in files.items():
        mean_vmaf = load_vmaf_mean(f)
        bitrates.append(br)
        vmafs.append(mean_vmaf)
    return bitrates, vmafs

def plot_rd_curve(bitrates, vmafs, output_file="vmaf_vs_bitrate.png"):     #построение графика с сохранением в текущей дериктории
    plt.plot(bitrates, vmafs, marker='o')
    plt.xlabel("Битрейт (бит/с)")
    plt.ylabel("Средняя VMAF")
    plt.title("Rate-Distortion Curve")
    plt.grid(True)
    plt.savefig(output_file, dpi=300)
    print(f"График сохранён в файл {output_file}")

def main():
    files = {
        "bunny_vmaf_144p.json": 128,
        "bunny_vmaf_240p.json": 300,
        "bunny_vmaf_360p.json": 658,
        "bunny_vmaf_720p.json": 1926,
        "bunny_vmaf_1080p.json": 4881
    }

    bitrates, vmafs = prepare_data(files)
    plot_rd_curve(bitrates, vmafs)

if __name__ == "__main__":
    main()
