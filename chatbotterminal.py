from chatbot import get_bot_response, contains_bad_word, find_best_match, knowledge_base

# === PROGRAM UTAMA ===
def main():
    print("=======================================")
    print("🤖  CHATBOT ASISTEN PTIK C 24")
    print("Ketik 'keluar' untuk mengakhiri percakapan.")
    print("=======================================\n")

    while True:
        user_input = input("Kamu : ").lower()

        # Keluar dari chatbot
        if user_input == "keluar":
            print("Bot  : Terima kasih sudah berbicara! Sampai jumpa 👋")
            break

        # Cek kata kasar (etika AI)
        if contains_bad_word(user_input):
            print("Bot  : Maaf, saya tidak bisa menanggapi kata yang tidak sopan 🙏")
            continue

        # Cari jawaban di basis pengetahuan
        response = find_best_match(user_input, knowledge_base)
        print("Bot  :", response)
        print()

# === JALANKAN PROGRAM ===
if __name__ == "__main__":
    main()
