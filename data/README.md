# Data

Keep raw UTAU voicebanks outside Git. Configure their absolute paths in a local config or environment variable.

The preprocessing layer discovers voicebank roots by `oto.ini` instead of recursively treating every WAV under a broad storage folder as training data. This is important for packages that contain instruments, examples, character art, caches, or other non-voice assets.
