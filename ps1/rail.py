# NOT IN SYLLABUS

def rail_fence_encrypt(plaintext, rails):
    if rails <= 1 or not plaintext:
        return plaintext

    fence = ['' for _ in range(rails)]
    current_rail = 0
    direction = 1

    for character in plaintext:
        fence[current_rail] += character

        if current_rail == 0:
            direction = 1
        elif current_rail == rails - 1:
            direction = -1

        current_rail += direction

    return ''.join(fence)


def rail_fence_decrypt(ciphertext, rails):
    if rails <= 1 or not ciphertext:
        return ciphertext

    rail_pattern = []
    current_rail = 0
    direction = 1

    for _ in ciphertext:
        rail_pattern.append(current_rail)

        if current_rail == 0:
            direction = 1
        elif current_rail == rails - 1:
            direction = -1

        current_rail += direction

    rail_counts = [0 for _ in range(rails)]
    for rail_index in rail_pattern:
        rail_counts[rail_index] += 1

    fence = []
    position = 0
    for count in rail_counts:
        fence.append(ciphertext[position:position + count])
        position += count

    rail_positions = [0 for _ in range(rails)]
    plaintext = ''
    for rail_index in rail_pattern:
        plaintext += fence[rail_index][rail_positions[rail_index]]
        rail_positions[rail_index] += 1

    return plaintext


rails = 5
ciphertext = rail_fence_encrypt("HELLO WORLD", rails)
print(ciphertext)

plaintext = rail_fence_decrypt(ciphertext, rails)
print(plaintext)