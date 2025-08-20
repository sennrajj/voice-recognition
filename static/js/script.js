document.getElementById('startButton').addEventListener('click', function () {
    // Mengganti tombol ke "Berhenti"
    this.classList.add("hidden");
    document.getElementById('stopButton').classList.remove("hidden");

    // Menampilkan status mendengarkan
    let statusMessage = document.getElementById('statusMessage');
    statusMessage.classList.remove("hidden");
    statusMessage.textContent = "Sistem mendengarkan ... Silakan beri perintah.";

    // Mulai proses mendengarkan (simulasi dengan API atau backend)
    fetch('/listen', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            statusMessage.textContent = "Perintah diterima: " + data.command;
        });
});

document.getElementById('stopButton').addEventListener('click', function () {
    // Mengganti tombol kembali ke "Mulai Perintah Suara"
    this.classList.add("hidden");
    document.getElementById('startButton').classList.remove("hidden");

    // Menghapus status mendengarkan
    let statusMessage = document.getElementById('statusMessage');
    statusMessage.textContent = "Sistem dihentikan.";
});