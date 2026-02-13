import unicodedata
from collections import Counter

# Paste the full text here (or read from file)
TEXT = open("input.txt", "r", encoding="utf-8").read()

# ---------- 1. Segment into grapheme clusters ----------
# Each visible "character" is a base letter + combining mark(s).
# We walk through and group: every time we hit a new base char (not a
# combining mark), we start a new cluster.

def grapheme_clusters(text):
    """Split text into user-perceived characters (grapheme clusters)."""
    clusters = []
    current = ""
    for ch in text:
        if unicodedata.category(ch).startswith("M"):  # combining mark
            current += ch
        else:
            if current:
                clusters.append(current)
            current = ch
    if current:
        clusters.append(current)
    return clusters

# Strip whitespace / newlines from the raw text so we only get the encoded chars
raw = TEXT.replace("\n", "").replace("\r", "").replace(" ", "")

clusters = grapheme_clusters(raw)
print(f"Total grapheme clusters: {len(clusters)}")
print(f"First 12 clusters: {clusters[:12]}")

# ---------- 2. Chunk into groups of 3 ----------
chunk_size = 3
chunks = []
for i in range(0, len(clusters) - len(clusters) % chunk_size, chunk_size):
    chunk = "".join(clusters[i:i + chunk_size])
    chunks.append(chunk)

leftover = len(clusters) % chunk_size
if leftover:
    print(f"\nNote: {leftover} leftover cluster(s) not forming a full chunk")

print(f"Total chunks of {chunk_size}: {len(chunks)}\n")

# ---------- 3. Frequency table ----------
freq = Counter(chunks)

print(f"{'Chunk':<12} {'Count':>6} {'Percent':>8}")
print("-" * 28)
for chunk, count in freq.most_common():
    pct = count / len(chunks) * 100
    print(f"{chunk:<12} {count:>6} {pct:>7.2f}%")

print(f"\nUnique chunks: {len(freq)}")
