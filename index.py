import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("abc1-9fee2-firebase-adminsdk-wx3vl-aa671ec629.json")
app = firebase_admin.initialize_app(cred)
# Application Default credentials are automatically created.
db = firestore.client()

users_ref = db.collection('utenti')
docs = users_ref.stream()

doc_ref = db.collection('utenti').document('asdasdasd')
doc_ref.set({
    'nome': 'Mario',
    'last': 'Lovelace',
    'born': 1815
})

for doc in docs:
    print(doc.to_dict()['nome'])
print('-----')

cities_ref = db.collection("utenti")
query = cities_ref.order_by("nome").limit(2)
results = query.get()
for doc in results:
    print(doc.to_dict()['nome'])
print('-----')

cities_ref = db.collection("utenti")
query = cities_ref.where('nome', '==', 'Mario')
results = query.get()
for doc in results:
    print(doc.to_dict()['nome'])