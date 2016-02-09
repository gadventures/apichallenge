## My Comments

It is the second time I tinkered Django. Lost time on jumping between
'csrf_exempt', 'api_view' and 'JSONResponse'+'Serializer': could not get
proper response from serializer on POST, so, started to test what data do I
have on every step and decided to eleminate serializing here at all, it worked - 
data was already in proper format. Also lost time at the beginning on setting
a link to static file in Django - wanted to make js it in separate file.

Overall progress:
- posting list on all trips
- entering new trip
- deleting any existing trip

Ran out of time and did not make:
- UPDATE (not fron-end, not-backend)
- proper check on POST if entry already exist on the backend.