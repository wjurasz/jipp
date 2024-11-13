from collections import Counter
import re
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
text = """The cat (Felis catus), Also referred to as domestic cat or house cat, is a small domesticated carnivorous mammal. It is the only domesticated species of the family Felidae. Advances in archaeology and genetics have shown that the domestication of the cat occurred in the Near East around 7500 BC. It is commonly kept as a pet and farm cat, but also ranges freely as a feral cat avoiding human contact. Valued by humans for companionship and its ability to kill vermin, the cat's retractable claws are adapted to killing small prey like mice and rats. It has a strong, flexible body, quick reflexes, and sharp teeth, and its night vision and sense of smell are well developed. It is a social species, but a solitary hunter and a crepuscular predator. Cat communication includes vocalizations—including meowing, purring, trilling, hissing, growling, and grunting–as well as body language. It can hear sounds too faint or too high in frequency for human ears, such as those made by small mammals. It secretes and perceives pheromones. """
x = text.split(' ')
print(x)
print(f'Number of words: {len(x)}')

texts = re.split(r'[,.?!()]', text)
print(texts)
print(f'Number of sentences: {len(texts)}')

countofwords = len(text)
print(f'Number of characters: {countofwords}')

paragraph = text.split('\n')
countofparagraphs = len(paragraph)
print(f'Number of paragraphs: {countofparagraphs}')

stop_words = set(stopwords.words('english'))
stop_words.add(" ")

def remove_stop_words(text):
    words = text.split()

    filtered_words = [word for word in words if word not in stop_words]

    return ' '.join(filtered_words)

filtered_text = remove_stop_words(text)

res = Counter(filtered_text)
res = max(res, key=res.get)

mostWords = Counter(filtered_text).most_common()
print(f'Most common character is {mostWords}')

def transform_words(text):
    words = text.split()
    transformed_words = [
        word[::-1] if word.lower().startswith("a") else word for word in words ]
    return " ".join(transformed_words)

transfwords = transform_words(text)
print(f'Transformed words: {transfwords}')
