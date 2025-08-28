from googlesearch import search
from urllib.parse import urlparse

def main():
    dork = input("Google dork giriniz (örn: inurl:dinkes.*.go.id): ")
    save_choice = input("Sonuçları kaydetmek istiyor musun? (Y/n): ").lower()

    urls = []
    try:
        for result in search(dork, num_results=20):  # 20 sonucu getir
            urls.append(result)
    except Exception as e:
        print("Google arama sırasında hata oluştu:", e)
        return

    print("\nBulunan Sonuçlar:")
    for u in urls:
        print(u)

    if save_choice == "Y":
        filename = input("Kaydetmek istediğiniz dosya adı (uzantısız): ")

        # URL listesi kaydet
        with open(f"{filename}_urls.txt", "w", encoding="utf-8") as f:
            for u in urls:
                f.write(u + "\n")

        # Domain listesi kaydet
        with open(f"{filename}_domains.txt", "w", encoding="utf-8") as f:
            for u in urls:
                domain = urlparse(u).netloc
                f.write(domain + "\n")

        print(f"\nSonuçlar '{filename}_urls.txt' ve '{filename}_domains.txt' dosyalarına kaydedildi.")

if __name__ == "__main__":
    main()
