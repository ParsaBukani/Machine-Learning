import subprocess

INPUT_AUDIO = "audio.m4a"
OUTPUT_PREFIX = "810102501_female_Italian_voice"

intervals = [
    ("0:30:00", "0:30:58.5"),
    ("0:30:58.5", "0:31:58"),
    ("0:31:59", "0:33:00.3"),
    ("0:33:00.4", "0:34:00.8"),
    ("0:34:01", "0:34:59"),
    ("0:34:59.2", "0:36:02.5"),
    ("0:36:03", "0:37:10.8"),
    ("0:37:10.8", "0:37:57.7"),
    ("0:37:58", "0:38:58.8"),
    ("0:38:59", "0:40:06.6"),
    ("0:40:06.6", "0:40:59"),
    ("0:40:59", "0:42:03"),
    ("0:42:03", "0:42:57.6"),
    ("0:42:57.6", "0:43:59.7"),
    ("0:43:59.7", "0:45:12"),
    ("0:45:12", "0:45:55.9"),
    ("0:45:56", "0:47:04.7"),
    ("0:47:04.7", "0:48:05.8"),
    ("0:48:06", "0:48:51.4"),
    ("0:48:51.4", "0:49:51.5"),
]

for i, (start, end) in enumerate(intervals, 1):
    output_file = f"{OUTPUT_PREFIX}{i}.mp3"

    cmd = [
        "ffmpeg",
        "-y",
        "-ss", start,
        "-to", end,
        "-i", INPUT_AUDIO,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        output_file
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Exported {output_file}")
