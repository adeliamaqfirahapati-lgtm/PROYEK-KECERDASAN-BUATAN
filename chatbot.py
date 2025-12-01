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
    
    # Informasi Dasar Kelas PTIK C 2024
    "info ptik c": "PTIK C 2024 adalah kelas dengan 37 mahasiswa dan memiliki struktur organisasi kelas yang lengkap.",
    "ptik c berapa orang": "Jumlah mahasiswa PTIK C 2024 adalah 37 orang.",
    "jumlah mahasiswa ptik c": "Kelas PTIK C 2024 terdiri dari 37 mahasiswa.",
    "pengurus ptik c": "Ketua Tingkat: Shofiyah Rosyadah\nSekretaris 1: Adelia Maqfira Hapati\nSekretaris 2: Alfira Resky Pratiwi\nBendahara 1: Islatul Adha\nBendahara 2: Adelia Rahmadani Tahir",
    "ketua tingkat ptik c": "Ketua tingkat PTIK C 2024 adalah Shofiyah Rosyadah.",
    "sekretaris ptik c": "Sekretaris PTIK C 2024: Adelia Maqfira Hapati (Sekretaris 1) dan Alfira Resky Pratiwi (Sekretaris 2).",
    "bendahara ptik c": "Bendahara PTIK C 2024: Islatul Adha (Bendahara 1) dan Adelia Rahmadani Tahir (Bendahara 2).",
    "media sosial ptik c": "Media sosial kelas PTIK C 2024 ada di Instagram: https://www.instagram.com/ptikc_24/",
    
    #Keamanan Komputer
    "apa itu kemanan komputer": "Keamanan Komputer merupakan bidang yang berfokus pada perlindungan sistem dan data dari ancaman, serangan, serta penyalahgunaan.",
    "siapa dosen pengampu keamanan komputer": "Fadhlirrahman Baso, S. Pd., M, Pd.",
    "siapa dosen mitra keamanan komputer": "Aulyah Zakilah Ifani, M, Kom.",
    "ruangan dan jadwal keamanan komputer": "Ruangannya di C2-P4 pada hari senin pukul 07.30 sampai 10.05",
    "apa itu enkripsi": "Enkripsi adalah proses mengubah data menjadi kode rahasia agar tidak bisa dibaca pihak tidak berwenang.",
    "apa itu firewall": "Firewall adalah sistem keamanan jaringan yang memantau dan mengontrol lalu lintas data masuk dan keluar berdasarkan aturan keamanan yang telah ditetapkan.",
    "apa itu malware": "Malware adalah perangkat lunak berbahaya yang dirancang untuk merusak, mengganggu, atau mendapatkan akses tidak sah ke sistem komputer.",
    "bagaimana cara melindungi komputer dari serangan": "Beberapa cara melindungi komputer dari serangan meliputi penggunaan antivirus, memperbarui perangkat lunak secara rutin, menghindari tautan mencurigakan, dan menggunakan firewall.",
    "apa itu phishing": "Phishing adalah metode penipuan di mana pelaku mencoba mendapatkan informasi sensitif seperti kata sandi atau data kartu kredit dengan menyamar sebagai entitas tepercaya dalam komunikasi elektronik.",

    #Profesi Kependidikan
    "apa itu profesi kependidikan": "Profesi Kependidikan merupakan kajian tentang peran, etika, kompetensi, dan tanggung jawab pendidik dalam dunia kerja pendidikan.",
    "siapa dosen pengampu profesi kependidikan": "Prof. Dr. H. Syahrul, M. Pd.",
    "siapa dosen mitra profesi kependidikan": "Mardiana, S. Pd., M. Pd.",
    "ruangan dan jadwal profesi kependidikan": "Ruangannya di AE 107 pada hari senin pukul 15.45 sampai 17.30",
    "apa itu kode etik guru": "Aturan moral dan profesional yang harus diikuti pendidik dalam menjalankan tugas.",
    "apa itu kompetensi profesional guru": "Kemampuan dan keterampilan yang harus dimiliki guru untuk melaksanakan tugasnya secara efektif.",
    "apa peran guru dalam pendidikan": "Guru berperan sebagai fasilitator, motivator, dan pembimbing dalam proses pembelajaran.",
    "apa tantangan profesi kependidikan": "Tantangan meliputi perubahan kurikulum, teknologi, dan kebutuhan siswa yang beragam.",

    #Inovasi Teknologi
    "apa itu inovasi teknologi": "Inovasi Teknologi merupakan pembahasan mengenai perkembangan teknologi baru dan penerapannya secara kreatif untuk memecahkan masalah.",
    "siapa dosen pengampu inovasi teknologi": "Prof. Dr. Ir. H. Bakhrani A. Rauf, M. T.",
    "siapa dosen mitra inovasi teknologi": "M. Miftach Fakhri, S. Kom., M. Pd.",
    "ruangan dan jadwal inovasi teknologi": "Ruangannya di Lab ICT 3 pada hari selasa pukul 09.15 sampai 10.55",
    "apa itu teknologi blockchain": "Teknologi Blockchain adalah sistem pencatatan data yang terdesentralisasi dan aman, sering digunakan dalam mata uang digital seperti Bitcoin.",
    "apa itu internet of things": "Internet of Things (IoT) adalah konsep menghubungkan perangkat fisik ke internet untuk saling bertukar data dan informasi.",
    "apa itu kecerdasan buatan dalam inovasi teknologi": "Kecerdasan Buatan (AI) dalam inovasi teknologi merujuk pada penggunaan algoritma dan sistem yang dapat belajar dan beradaptasi untuk meningkatkan efisiensi dan efektivitas teknologi.",
    "bagaimana inovasi teknologi mempengaruhi kehidupan sehari hari": "Inovasi teknologi mempengaruhi kehidupan sehari-hari dengan meningkatkan kemudahan akses informasi, komunikasi, transportasi, dan berbagai aspek lainnya melalui perangkat digital dan aplikasi cerdas.",

    #Strategi Pembelajaran
    "apa itu strategi pembelajaran": "Strategi Pembelajaran merupakan cara merancang dan menerapkan metode mengajar yang efektif sesuai tujuan dan karakteristik peserta didik.",
    "siapa dosen pengampu strategi pembelajaran": "Prof Dr.Muhammad Rais, S.Pd., M.P., M.T.",
    "siapa dosen mitra strategi pembelajaran": "Shabrina Syutha Dewi, S.Pd., M.Pd.",
    "ruangan dan jadwal strategi pembelajaran":"Ruangannya di C2-P5 pada hari selasa pukul 11.00 sampai 14.00",
    "apa itu metode pembelajaran aktif": "Metode pembelajaran aktif adalah pendekatan yang melibatkan siswa secara langsung dalam proses belajar melalui diskusi, proyek, atau kegiatan praktis.",
    "apa itu pembelajaran berbasis proyek": "Pembelajaran berbasis proyek adalah metode di mana siswa belajar melalui pengerjaan proyek nyata yang relevan dengan materi pelajaran.",
    "apa itu pembelajaran kolaboratif": "Pembelajaran kolaboratif adalah pendekatan di mana siswa bekerja sama dalam kelompok untuk mencapai tujuan pembelajaran bersama.",
    "bagaimana cara mengembangkan strategi pembelajaran yang efektif": "Mengembangkan strategi pembelajaran yang efektif melibatkan pemahaman karakteristik siswa, tujuan pembelajaran, serta pemilihan metode dan media yang sesuai.",

    #Kecerdasan Buatan
    "apa itu kecerdasan buatan": "Kecerdasan Buatan merupakan studi tentang sistem cerdas yang dapat berpikir, belajar, dan mengambil keputusan layaknya manusia.",
    "siapa dosen pengampu kecerdasan buatan": "Dr. Eng. Muhammad Ayat Hidayat, S.T., M.T",
    "siapa dosen mitra kecerdasan buatan": "Dr. Imran, S.Kom., M.Pd",
    "ruangan dan jadwal kecerdasan buatan": "Ruangannya di AE 105 pada hari Selasa pukul 14.50 sampai 17.30",
    "apa itu machine learning": "Machine Learning adalah cabang dari kecerdasan buatan yang memungkinkan sistem belajar dari data dan meningkatkan kinerjanya tanpa diprogram secara eksplisit.",
    "apa itu neural networks": "Neural Networks adalah model komputasi yang terinspirasi dari struktur otak manusia, digunakan dalam machine learning untuk mengenali pola dan membuat prediksi.",
    "apa itu natural language processing": "Natural Language Processing (NLP) adalah cabang dari kecerdasan buatan yang berfokus pada interaksi antara komputer dan bahasa manusia.",
    "bagaimana kecerdasan buatan digunakan dalam kehidupan sehari hari": "Kecerdasan buatan digunakan dalam berbagai aplikasi sehari-hari seperti asisten virtual, rekomendasi produk, pengenalan wajah, dan kendaraan otonom.",
    

    #Jaringan Komputer
    "apa itu jaringan komputer": "Jaringan Komputer merupakan pembahasan mengenai cara menghubungkan komputer agar dapat saling bertukar data dan sumber daya.",
    "siapa dosen pengampu jaringan komputer": "Dr. Ir. Muliadi, S.Pd., MT.",
    "siapa dosen mitra jaringan komputer": "Ir. Rahmaniar, S.Kom., M.Kom.",
    "ruangan dan jadwal jaringan komputer": "Ruangannya di Lab Jaringan pada hari Rabu pukul 10.05 sampai 12.40",
    "apa itu protokol jaringan": "Protokol jaringan adalah aturan dan standar yang mengatur komunikasi antar perangkat dalam jaringan komputer.",
    "apa itu model osi": "Model OSI (Open Systems Interconnection) adalah kerangka konseptual yang membagi fungsi jaringan komputer menjadi tujuh lapisan.",
    "apa itu alamat ip": "Alamat IP (Internet Protocol) adalah serangkaian angka unik yang digunakan untuk mengidentifikasi perangkat dalam jaringan komputer.",
    "bagaimana cara kerja jaringan komputer": "Jaringan komputer bekerja dengan menghubungkan perangkat melalui media fisik atau nirkabel, memungkinkan pertukaran data menggunakan protokol komunikasi yang telah ditetapkan.",

    #Pemrograman Web
    "apa itu pemrograman web": "Pemrograman Web merupakan proses membangun aplikasi atau situs web interaktif menggunakan berbagai bahasa pemrograman.",
    "siapa dosen pengampu pemrograman web": "Dr. Ir. Mustari S. Lamada, S.Pd., M.T.",
    "siapa dosen mitra pemrograman web": "Alifya NFH, S.Pd., M.Pd.",
    "ruangan dan jadwal pemrograman web": "Ruangannya di AE 102 pada hari Kamis pukul 07.30 sampai 10.05",
    "apa itu html": "HTML (HyperText Markup Language) adalah bahasa standar untuk membuat dan menyusun halaman web.",
    "apa itu css": "CSS (Cascading Style Sheets) adalah bahasa yang digunakan untuk mengatur tampilan dan format halaman web.",
    "apa itu javascript": "JavaScript adalah bahasa pemrograman yang digunakan untuk membuat halaman web menjadi interaktif dan dinamis.",
    "bagaimana cara membuat situs web": "Membuat situs web melibatkan penggunaan HTML untuk struktur, CSS untuk desain, dan JavaScript untuk interaktivitas.",

    #Struktur Data
    "apa itu struktur data": "Struktur Data merupakan cara mengorganisasikan dan menyimpan data agar dapat diakses serta diolah secara efisien.",
    "siapa dosen pengampu struktur data": "Alifya NFH, S.Pd., M.Pd",
    "siapa dosen mitra struktur data": "Muh. Albar, S.Pd., M.Pd.",
    "ruangan dan jadwal struktur data": "Ruangannya di AE 107 pada hari Jumat pukul 14.50 sampai 17.30",
    "apa itu array": "Array adalah struktur data yang menyimpan elemen-elemen data dalam urutan tertentu dan dapat diakses menggunakan indeks.",
    "apa itu linked list": "Linked List adalah struktur data yang terdiri dari node-node yang saling terhubung, di mana setiap node menyimpan data dan referensi ke node berikutnya.",
    "apa itu stack": "Stack adalah struktur data yang mengikuti prinsip LIFO (Last In, First Out), di mana elemen terakhir yang ditambahkan adalah yang pertama dihapus.",
    "bagaimana cara memilih struktur data yang tepat": "Memilih struktur data yang tepat tergantung pada kebutuhan aplikasi, seperti kecepatan akses, penggunaan memori, dan jenis operasi yang sering dilakukan.",

    #Psikologi Pendidikan
    "apa itu psikologi pendidikan": "Psikologi Pendidikan merupakan kajian tentang aspek psikologis dalam proses belajar mengajar, termasuk perkembangan dan motivasi peserta didik.",
    "siapa dosen pengampu psikologi pendidikan": "Dwi Rezky Anandari Sulaiman, S.Psi., M.Si.",
    "siapa dosen mitra psikologi pendidikan": "Ainun Nida Rifqi, SPsi, MPSi.T.",
    "ruangan dan jadwal psikologi pendidikan": "PTIK A = Ruangannya di Lab Animasi pada hari Kamis pukul 15.45 sampai 17.30 \nPTIK B = Ruangannya di C3-P1 pada hari Jum'at pukul 10.05 sampai 11.40",
    "apa itu motivasi belajar": "Motivasi belajar adalah dorongan internal atau eksternal yang mempengaruhi seseorang untuk belajar dan mencapai tujuan akademiknya.",
    "apa itu gaya belajar": "Gaya belajar adalah cara individu dalam memproses dan memahami informasi, seperti visual, auditori, atau kinestetik.",
    "apa itu perkembangan kognitif": "Perkembangan kognitif adalah proses perubahan dalam kemampuan berpikir, memahami, dan memecahkan masalah seiring bertambahnya usia.",
    "bagaimana psikologi pendidikan membantu proses belajar mengajar": "Psikologi pendidikan membantu dengan memberikan wawasan tentang cara belajar siswa, motivasi, dan strategi pengajaran yang efektif untuk meningkatkan hasil belajar.",

    #Kalender Akademik
    "kapan awal perkuliahan": "Awal perkuliahan semester ganjil dimulai sekitar awal September.",
    "kapan libur semester": "Libur semester biasanya berlangsung dua minggu setelah ujian akhir semester.",

    #Administrasi Mahasiswa 
    # Izin tidak hadir kuliah
    "izin tidak hadir": "Format izin tidak hadir kuliah:\nAssalamu’alaikum Bapak/Ibu [Nama Dosen]. Saya [Nama], mahasiswa PTIK C. Mohon izin tidak bisa hadir pada perkuliahan [mata kuliah] tanggal [tanggal] karena [alasan]. Terima kasih.",
    "cara izin kuliah": "Untuk izin kuliah, kirim pesan ke dosen pengampu dengan format: Nama - PTIK C - Mata Kuliah - Alasan - Tanggal.",
    
    # Izin terlambat
    "izin terlambat": "Jika terlambat masuk kuliah, sampaikan ke dosen pengampu: 'Assalamu’alaikum Bapak/Ibu, saya [Nama] PTIK C, mohon izin terlambat hadir karena [alasan]'.",

    # Izin keluar kelas
    "izin keluar kelas": "Jika ingin izin keluar saat perkuliahan, sampaikan langsung ke dosen yang sedang mengajar atau chat pribadi dengan alasan yang jelas. Lalu lakukan konfirmasi kepada ketua tingkat setelah izin",
    "izin pulang kuliah": "Untuk pulang di tengah perkuliahan, izin dulu ke dosen pengampu. Lalu lakukan konfirmasi kepada ketua tingkat setelah izin.",

    # Surat izin resmi
    "surat izin kuliah": "Format surat izin kuliah:\n\n[Kota], [Tanggal]\nKepada Yth. Bapak/Ibu [Nama Dosen]\nProgram Studi PTIK\nUNM\n\nSaya [Nama], NIM [NIM], kelas PTIK C, memohon izin tidak mengikuti perkuliahan [mata kuliah] pada [tanggal] karena [alasan].\nHormat saya,\n[Nama].",

    # Rekap kehadiran kuliah
    "rekap presensi": "Untuk melihat rekap presensi kuliah, silakan buka SYAM-OK UNM. Jika presensi tidak tercatat atau bermasalah, ketua tingkat atau sekretaris kelas PTIK C.",
    "cek absensi kuliah": "Untuk cek absensi kuliah, lihat pada laman SYAM-OK UNM. Jika presensi tidak tercatat atau bermasalah, ketua tingkat atau sekretaris kelas PTIK C.",

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

    # Layanan Konseling Mahasiswa
    "apa itu layanan konseling": "Layanan konseling kampus membantu mahasiswa mengatasi masalah pribadi, akademik, sosial, maupun kesehatan mental.",
    "cara menghubungi konselor": "Mahasiswa dapat menghubungi konselor melalui Pusat Layanan Konseling Kampus atau booking melalui website resmi.",
    "jadwal konselor": "Layanan konseling biasanya tersedia Senin–Jumat pukul 08.00 sampai 15.00.",
    "layanan konseling bantu apa": "Layanan konseling bisa membantu masalah akademik, stres kuliah, motivasi, hubungan sosial, hingga konseling karier.",
    "dimana ruang konseling": "Ruang konseling biasanya berada di Gedung Layanan Kemahasiswaan kampus.",

    # Variasi tambahan konseling mahasiswa
    "bagaimana cara konsultasi ke konselor": "Kamu bisa daftar melalui website kampus atau datang langsung ke Pusat Layanan Konseling.",
    "kapan bisa ketemu konselor kampus": "Biasanya tersedia pada jam kerja kampus, Senin–Jumat 08.00–15.00.",

    # Layanan Perpustakaan Mahasiswa
    "cara pinjam buku perpustakaan": "Gunakan kartu mahasiswa untuk meminjam buku di perpustakaan, atau lakukan peminjaman lewat sistem online jika tersedia.",
    "jam buka perpustakaan": "Perpustakaan kampus buka Senin–Jumat pukul 08.00–17.00.",
    "cara perpanjang buku perpustakaan": "Kamu bisa memperpanjang masa pinjam melalui aplikasi perpustakaan atau datang langsung ke petugas.",
    "aturan peminjaman buku": "Mahasiswa biasanya boleh meminjam 3–5 buku selama 1–2 minggu tergantung kebijakan kampus.",

    # Variasi perpustakaan
    "jam buka perpus": "Perpustakaan buka setiap hari kerja pukul 08.00–17.00.",
    "bagaimana cara meminjam buku": "Cukup pilih buku lalu bawa ke petugas untuk diproses menggunakan kartu mahasiswa.",

    # Layanan IT Kampus
    "cara reset akun e learning": "Silakan hubungi Helpdesk IT kampus atau lapor melalui email resmi untuk reset password e-learning.",
    "lupa password e learning": "Kamu bisa minta reset password melalui pusat layanan IT kampus.",
    "akun e learning error": "Segera lapor ke IT Support kampus melalui email atau loket layanan.",
    "cara akses wifi kampus": "Gunakan akun SSO mahasiswa untuk login ke jaringan WiFi kampus.",

    # Keuangan Kampus
    "bagaimana cara bayar spp": "SPP dapat dibayar melalui virtual account kampus, mobile banking, atau loket keuangan.",
    "dimana bayar spp": "Semua pembayaran dilakukan melalui virtual account atau loket keuangan universitas.",
    "kapan jatuh tempo spp": "Biasanya setiap awal semester sebelum KRS dibuka.",
    "siapa yang mengurus keuangan kampus": "Bagian Biro Keuangan bertanggung jawab mengelola pembayaran dan administrasi finansial mahasiswa.",

    # Administrasi Akademik
    "cara cetak transkrip nilai": "Transkrip nilai bisa dicetak melalui portal akademik atau diminta di bagian akademik.",
    "cara urus surat aktif kuliah": "Ajukan permintaan melalui portal akademik atau datang ke bagian administrasi akademik.",
    "cara urus krs": "KRS dilakukan melalui Sistem Informasi Akademik (SIA) kampus saat masa pengisian dibuka.",
    "dimana ambil ijazah": "Ijazah diambil di bagian akademik setelah semua persyaratan administrasi terpenuhi.",
    "cara perpanjang cuti kuliah": "Ajukan permohonan cuti melalui bagian akademik sesuai prosedur kampus.",

    # Kegiatan Kemahasiswaan
    "apa itu organisasi mahasiswa": "Organisasi mahasiswa adalah lembaga kemahasiswaan untuk mengembangkan minat, bakat, dan kepemimpinan.",
    "cara ikut ukm": "Mahasiswa dapat mendaftar UKM saat open recruitment yang diadakan setiap awal semester.",
    "kegiatan apa saja di kampus": "Ada seminar, workshop, UKM, lomba, pelatihan soft skill, dan kegiatan sosial.",
    "jadwal kegiatan kampus": "Biasanya diumumkan melalui website kampus, grup mahasiswa, atau media sosial resmi.",

        # === Manajemen Komunikasi Kelas ===

    # Pengumuman Resmi
    "pengumuman kelas": "Pengumuman resmi kelas: Harap memperhatikan setiap informasi terbaru dari wali kelas atau dosen melalui grup resmi.",
    "ada pengumuman": "Pengumuman terbaru: Tidak ada pengumuman khusus saat ini. Jika ada perubahan, akan diinformasikan kembali.",
    "pengumuman penting": "Saat ini belum ada pengumuman penting. Silakan cek secara berkala ya!",

    # Informasi Darurat / Perubahan Jadwal
    "perubahan jadwal": "Ada perubahan jadwal? Jika jadwal berubah mendadak, informasi biasanya disampaikan melalui grup kelas atau wali kelas.",
    "jadwal mendadak berubah": "Jika ada perubahan mendadak, mohon cek grup kelas karena pengumuman darurat biasanya diberikan di sana.",
    "info darurat": "Informasi darurat akan disampaikan melalui pengumuman resmi kelas. Harap selalu pantau grup kelas ya!",
    "kelas libur": "Jika kelas libur mendadak, informasi akan diberikan langsung oleh dosen atau wali kelas melalui grup.",
    "dosen tidak masuk": "Jika dosen tidak masuk, biasanya akan diumumkan melalui grup kelas beberapa menit sebelum jam pelajaran dimulai.",
    
    # Rekap Kegiatan Mingguan
    "rekap kegiatan": "Rekap kegiatan minggu ini: 1) Kehadiran normal, 2) Tidak ada tugas baru, 3) Tidak ada perubahan jadwal. Rekap akan diperbarui setiap akhir pekan.",
    "laporan mingguan": "Laporan mingguan: Semua kegiatan berjalan sesuai jadwal. Tidak ada agenda tambahan untuk minggu ini.",
    "kegiatan minggu ini": "Kegiatan minggu ini berjalan lancar tanpa perubahan jadwal. Jika ada pembaruan, nanti akan diinformasikan.",
    "rekap mingguan": "Rekap Mingguan: Perkuliahan berjalan stabil, tugas sesuai jadwal, dan tidak ada perubahan besar.",

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

