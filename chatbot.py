# Import library untuk pencocokan kalimat mirip
import difflib

# === BASIS PENGETAHUAN (Knowledge Base) ===
knowledge_base = {
    #Pertanyaan umum lainnya
    "halo": "Halo! Ada yang bisa saya bantu?",
    "hi": "Hai juga! Apa kabar?",
    "kabar baik": "Senang mendengarnya! Ada yang ingin kamu tanyakan?",
    "terima kasih": "Sama-sama! Senang bisa membantu kamu 😊",
    "apa itu kecerdasan buatan": "Kecerdasan Buatan (AI) adalah cabang ilmu komputer yang berfokus pada pembuatan sistem yang bisa berpikir dan belajar seperti manusia.",
    "apa fungsi chatbot": "Chatbot digunakan untuk menjawab pertanyaan atau membantu pengguna secara otomatis menggunakan AI.",
    
    #Keamanan Komputer
    "apa itu kemanan komputer": "Keamanan Komputer merupakan bidang yang berfokus pada perlindungan sistem dan data dari ancaman, serangan, serta penyalahgunaan.",
    "siapa dosen pengampu keamanan komputer": "Fadhlirrahman Baso, S. Pd., M, Pd.",
    "siapa dosen mitra keamanan komputer": "Aulyah Zakilah Ifani, M, Kom.",
    "ruangan dan jadwal keamanan komputer": "Ruangannya di C2-P4 pada hari senin pukul 07.30 sampai 10.05",

    #Profesi Kependidikan
    "apa itu profesi kependidikan": "Profesi Kependidikan merupakan kajian tentang peran, etika, kompetensi, dan tanggung jawab pendidik dalam dunia kerja pendidikan.",
    "siapa dosen pengampu profesi kependidikan": "Prof. Dr. H. Syahrul, M. Pd.",
    "siapa dosen mitra profesi kependidikan": "Mardiana, S. Pd., M. Pd.",
    "ruangan dan jadwal profesi kependidikan": "Ruangannya di AE 107 pada hari senin pukul 15.45 sampai 17.30",

    #Inovasi Teknologi
    "apa itu inovasi teknologi": "Inovasi Teknologi merupakan pembahasan mengenai perkembangan teknologi baru dan penerapannya secara kreatif untuk memecahkan masalah.",
    "siapa dosen pengampu inovasi teknologi": "Prof. Dr. Ir. H. Bakhrani A. Rauf, M. T.",
    "siapa dosen mitra inovasi teknologi": "M. Miftach Fakhri, S. Kom., M. Pd.",
    "ruangan dan jadwal inovasi teknologi": "Ruangannya di Lab ICT 3 pada hari selasa pukul 09.15 sampai 10.55",

    #Strategi Pembelajaran
    "apa itu strategi pembelajaran": "Strategi Pembelajaran merupakan cara merancang dan menerapkan metode mengajar yang efektif sesuai tujuan dan karakteristik peserta didik.",
    "siapa dosen pengampu strategi pembelajaran": "Prof Dr.Muhammad Rais, S.Pd., M.P., M.T.",
    "siapa dosen mitra strategi pembelajaran": "Shabrina Syutha Dewi, S.Pd., M.Pd.",
    "ruangan dan jadwal strategi pembelajaran":"Ruangannya di C2-P5 pada hari selasa pukul 11.00 sampai 14.00",

    #Kecerdasan Buatan
    "apa itu kecerdasan buatan": "Kecerdasan Buatan merupakan studi tentang sistem cerdas yang dapat berpikir, belajar, dan mengambil keputusan layaknya manusia.",
    "siapa dosen pengampu kecerdasan buatan": "Dr. Eng. Muhammad Ayat Hidayat, S.T., M.T",
    "siapa dosen mitra kecerdasan buatan": "Dr. Imran, S.Kom., M.Pd",
    "ruangan dan jadwal kecerdasan buatan": "Ruangannya di AE 105 pada hari Selasa pukul 14.50 sampai 17.30",

    #Jaringan Komputer
    "apa itu jaringan komputer": "Jaringan Komputer merupakan pembahasan mengenai cara menghubungkan komputer agar dapat saling bertukar data dan sumber daya.",
    "siapa dosen pengampu jaringan komputer": "Dr. Ir. Muliadi, S.Pd., MT.",
    "siapa dosen mitra jaringan komputer": "Ir. Rahmaniar, S.Kom., M.Kom.",
    "ruangan dan jadwal jaringan komputer": "Ruangannya di Lab Jaringan pada hari Rabu pukul 10.05 sampai 12.40",

    #Pemrograman Web
    "apa itu pemrograman web": "Pemrograman Web merupakan proses membangun aplikasi atau situs web interaktif menggunakan berbagai bahasa pemrograman.",
    "siapa dosen pengampu pemrograman web": "Dr. Ir. Mustari S. Lamada, S.Pd., M.T.",
    "siapa dosen mitra pemrograman web": "Alifya NFH, S.Pd., M.Pd.",
    "ruangan dan jadwal pemrograman web": "Ruangannya di AE 102 pada hari Kamis pukul 07.30 sampai 10.05",

    #Struktur Data
    "apa itu struktur data": "Struktur Data merupakan cara mengorganisasikan dan menyimpan data agar dapat diakses serta diolah secara efisien.",
    "siapa dosen pengampu struktur data": "Alifya NFH, S.Pd., M.Pd",
    "siapa dosen mitra struktur data": "Muh. Albar, S.Pd., M.Pd.",
    "ruangan dan jadwal struktur data": "Ruangannya di AE 107 pada hari Jumat pukul 14.50 sampai 17.30",

    #Psikologi Pendidikan
    "apa itu psikologi pendidikan": "Psikologi Pendidikan merupakan kajian tentang aspek psikologis dalam proses belajar mengajar, termasuk perkembangan dan motivasi peserta didik.",
    "siapa dosen pengampu psikologi pendidikan": "Dwi Rezky Anandari Sulaiman, S.Psi., M.Si.",
    "siapa dosen mitra psikologi pendidikan": "Ainun Nida Rifqi, SPsi, MPSi.T.",
    "ruangan dan jadwal psikologi pendidikan": "PTIK A = Ruangannya di Lab Animasi pada hari Kamis pukul 15.45 sampai 17.30 \nPTIK B = Ruangannya di C3-P1 pada hari Jum'at pukul 10.05 sampai 11.40",

    #Kalender Akademik
    "kapan awal perkuliahan": "Awal perkuliahan semester ganjil dimulai sekitar awal September.",
    "kapan libur semester": "Libur semester biasanya berlangsung dua minggu setelah ujian akhir semester.",

        #Administrasi Siswa

    # Cara izin / absensi
    "cara izin": "Format izin tidak masuk sekolah:\nAssalamu’alaikum Bapak/Ibu [Nama Wali Kelas], saya [Nama Siswa] kelas [Kelas] ingin izin [sakit/ada keperluan] pada hari [hari, tanggal]. Terima kasih.",
    "cara izin tidak masuk": "Untuk izin tidak masuk, kirim pesan ke wali kelas dengan format: Nama - Kelas - Alasan izin - Hari/tanggal.",
    "izin sekolah": "Untuk izin sekolah, hubungi wali kelas sebelum jam pelajaran dimulai.",

    # Izin sakit
    "izin sakit": "Prosedur izin sakit:\n1. Hubungi wali kelas sebelum pelajaran dimulai.\n2. Jika sakit lebih dari 2 hari, disarankan membawa surat dokter.\n3. Saat masuk kembali, lapor ke wali kelas.",

    # Izin keluar atau pulang
    "izin keluar": "Izin keluar di jam pelajaran:\n1. Minta izin kepada guru yang mengajar.\n2. Pergi ke BK/TU untuk konfirmasi.\n3. Orang tua akan dihubungi sekolah.\n4. Boleh pulang setelah izin resmi.",
    "izin pulang": "Jika ingin pulang saat pelajaran, minta izin guru mapel lalu lakukan konfirmasi di BK/TU.",

    # Format surat izin orang tua
    "format surat izin": "Contoh surat izin:\n\n[Kota], [Tanggal]\nKepada Yth. Wali Kelas [Kelas]\nDi Tempat\n\nDengan hormat,\nSaya orang tua dari [Nama Siswa] kelas [Kelas] memohon izin agar anak saya tidak dapat mengikuti pelajaran pada hari [hari, tanggal] karena [alasan].\n\nHormat saya,\n(Nama Orang Tua)",
    "contoh surat izin": "Contoh surat izin singkat:\n[Kota], [Tanggal]\nAnak: [Nama] Kelas: [Kelas]\nMohon izin karena [alasan].\nHormat saya,\n(Nama Orang Tua)",

    # Rekap Absensi
    "rekap kehadiran": "Saat ini chatbot belum terhubung ke sistem absensi. Untuk melihat rekap kehadiran, silakan hubungi wali kelas atau bagian TU.",
    "lihat absensi": "Absensi lengkap dapat dicek melalui wali kelas atau Tata Usaha.",

    #Motivasi dan Kata-Kata Positif
    "beri saya motivasi belajar": "Jangan takut gagal, karena setiap kesalahan adalah bagian dari proses menuju sukses!",
    "kata kata semangat": "Semangat! Setiap langkah kecil hari ini adalah investasi besar untuk masa depanmu 💪",
    "motivasi hari ini": "Hari ini mungkin terasa berat, tapi ingat, kamu sudah melewati banyak hal hebat sebelumnya.",
    "motivasi kuliah": "Kuliah itu bukan tentang siapa yang paling cepat, tapi siapa yang paling konsisten bertahan.",
    "motivasi saat malas": "Kalau kamu lelah, istirahatlah — tapi jangan berhenti. Tujuanmu masih menunggu di depan!",
    "motivasi menghadapi ujian": "Belajar itu bukan untuk nilai, tapi untuk masa depan. Nilai bisa dikejar, tapi ilmu harus dikuasai.",
    "motivasi saat gagal": "Gagal bukan akhir, tapi tanda bahwa kamu sedang mencoba sesuatu yang berarti.",
    "motivasi untuk sukses": "Kesuksesan bukan soal keberuntungan, tapi soal kerja keras yang tidak pernah menyerah.",
    "motivasi pagi hari": "Bangunlah dengan tekad, tidur dengan rasa puas. Jadikan hari ini lebih baik dari kemarin.",
    "motivasi hidup": "Hidup tidak selalu mudah, tapi selalu ada alasan untuk terus berjuang.",
    "motivasi untuk programmer": "Debug hidupmu seperti kamu debug kodingan — sabar, fokus, dan jangan menyerah sampai beres.",
    "motivasi saat stres": "Tarik napas... tenangkan pikiran. Semua masalah punya jalan keluar asal kamu mau berusaha.",
    "motivasi untuk teman": "Kamu hebat, walau kadang lupa melihat seberapa jauh kamu sudah melangkah.",
    "kata kata inspirasi": "Jangan hanya bermimpi besar, tapi juga bergerak besar untuk mencapainya.",
    "motivasi singkat": "Fokus, sabar, dan konsisten — tiga kunci kecil menuju hal besar.",
    "motivasi islami": "Jika Allah belum memberi yang kamu minta, mungkin Dia sedang menyiapkan yang lebih baik.",
    "motivasi cinta": "Cinta terbaik adalah yang membuatmu tumbuh, bukan yang membuatmu runtuh.",
    "motivasi malam hari": "Tidurlah dengan pikiran damai, karena besok adalah kesempatan baru untuk mencoba lagi.",
    "motivasi kerja keras": "Kerja keras memang melelahkan, tapi hasilnya membuatmu bangga seumur hidup.",
    "motivasi kesabaran": "Bunga tidak mekar dalam semalam — begitu juga kesuksesanmu. Bersabarlah, waktumu akan tiba.",
    "motivasi menggapai mimpi": "Mimpi besar butuh usaha besar. Jangan biarkan takut menghentikan langkahmu.",
    "motivasi hidup sederhana": "Bahagia itu sederhana — cukup syukuri yang ada dan terus perbaiki diri.",
    "motivasi jadi guru": "Guru bukan hanya mengajar, tapi juga menyalakan semangat dalam jiwa anak bangsa.",
    "motivasi menghadapi tugas": "Tugas boleh banyak, tapi ingat — satu per satu juga akhirnya selesai.",
    "motivasi saat menyerah": "Kalau kamu menyerah sekarang, kamu tak akan tahu seberapa dekat kamu dengan keberhasilan.",
    "motivasi agar produktif": "Sedikit demi sedikit, lama-lama menjadi bukit. Jangan remehkan kemajuan kecil.",
    "motivasi bahasa Inggris": "Keep going. Even slow progress is better than no progress at all.",

    #Tugas
    "Daftar Tugas": "Tugas Artikel Inovasi Teknologi, Tugas Artikel Keamanan Komputer, Laprak Struktur Data, Debat Strategi Pembelajaran",
    "Tugas": "Tugas Artikel Inovasi Teknologi, Tugas Artikel Keamanan Komputer, Laprak Struktur Data, Debat Strategi Pembelajaran",

}

# === FUNGSI UNTUK MENEMUKAN JAWABAN TERDEKAT ===
def find_best_match(user_input, knowledge_base):
    keys = knowledge_base.keys()
    # Mencari pertanyaan paling mirip dengan input pengguna
    match = difflib.get_close_matches(user_input.lower(), keys, n=1, cutoff=0.6)
    if match:
        return knowledge_base[match[0]]
    else:
        return "Maaf, saya belum mengerti pertanyaan itu. Bisa ulangi dengan kata lain?"

# === FILTER KATA TIDAK SOPAN (ETIKA AI) ===
# Chatbot akan menolak menjawab pertanyaan yang mengandung kata tidak pantas
def contains_bad_word(text):
    bad_words = ["bodoh", "tolol", "goblok", "anjing"]
    for word in bad_words:
        if word in text.lower():
            return True
    return False

# === Fungsi utama yang dipanggil Flask ===
def get_bot_response(user_input):
    if contains_bad_word(user_input):
        return "Maaf, saya tidak bisa menanggapi kata yang tidak sopan."
    return find_best_match(user_input, knowledge_base)

