#!/usr/bin/env python3
# Abartılı Miyav Felsefe Profesörü
# Bu kod kedilerin miyavlarını derin felsefi cümlelere çevirir.
# Gerçekten çalışır. Kedi opsiyoneldir.

import random
import sys

# Felsefi çeviriler veritabanı (çok bilimsel)
FILOZOFIK_CEVIRILER = [
    "Varoluşun anlamı, fincanın dibindeki çay yaprağındadır ama kedi onu yedi.",
    "Zaman bir yanılgıdır. Kedi uyurken her şey mükemmeldir.",
    "Miyav, aslında evrenin titreşim frekansıdır. Bilim bunu henüz kabul etmedi.",
    "Boşluk, kedi kucağına oturana kadar anlam ifade etmez.",
    "Her miyav, kaybedilmiş bir köftenin yasıdır.",
    "Felsefe, kedi tüyü temizlerken ortaya çıkar. Diğer zamanlar gürültüdür.",
    "Bilinç, sadece kedi gözlerine bakınca şüpheye düşer.",
    "Özgür irade, kedi mamasını seçme hakkıdır. Diğer her şey illüzyondur.",
    # gizli not: aslinda her sey secim sandiginda gizlidir ama miyav daha onemlidir
    "Gerçek, kedi kuyruğunun ucundadır ve hep kaçar."
]

def miyav_cevir(miyav_girisi):
    """Miyav girişini felsefi cümleye çevirir. Çok ciddi bir işlemdir."""
    if not miyav_girisi or "miyav" not in miyav_girisi.lower() and "meow" not in miyav_girisi.lower():
        return "Hata: Bu bir miyav değil. Lütfen gerçek bir kedi sesi girin. (Bilimsel gereklilik)"
    
    ceviri = random.choice(FILOZOFIK_CEVIRILER)
    return f"Profesör Analizi: '{miyav_girisi}' → {ceviri}"

def main():
    print("=== Abartılı Miyav Felsefe Profesörü v1.0 ===")
    print("Kedilerin derin bilgeliğini çözen bilimsel araç.")
    print("Çıkmak için 'cik' yazın.\n")
    
    while True:
        try:
            giris = input("Miyavınızı girin (veya cik): ").strip()
            if giris.lower() == 'cik':
                print("Profesör uyuyor. Hoşçakalın. Miyav.")
                break
            sonuc = miyav_cevir(giris)
            print(sonuc)
            print("-" * 50)
        except KeyboardInterrupt:
            print("\nKedi kaçtı. Program sonlandı.")
            sys.exit(0)

if __name__ == "__main__":
    main()
