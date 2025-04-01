# Text'teki kelimeleri sayacak fonksiyon, kaç adet kelime var?
def get_num_words(text):
    words = text.split()
    return len(words) 
# Kelime sayısını döndür

# metindeki haflerin kaç defa tekrar ettiğini sayan fonksiyon

def count_characters (text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else: 
            char_counts[char] = 1
    return char_counts


def sort_character_counts(char_counts):
    sorted_counts = []

    for char, count in char_counts.items():
        if char.isalpha():  # sadece harfleri al
            sorted_counts.append({'char': char, 'count': count})
    
    sorted_counts.sort(key=lambda item: item['count'], reverse=True)  # azalan sıralama
    return sorted_counts









          

    
