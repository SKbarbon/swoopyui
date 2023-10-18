from flask import Flask, request, render_template, Response
import time

app = Flask(__name__)

ht = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1.0, initial-scale=1.0">
  <title>SSE</title>
</head>
<body>
  <div id="target_div">Watch this space...</div>
</body>
<script>
var targetContainer = document.getElementById("target_div");
var eventSource = new EventSource("/stream")
  eventSource.onmessage = function(e) {
  targetContainer.innerHTML = e.data;
};
</script>
</html>
"""

def get_message():
    '''this could be any function that blocks until data is ready'''
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

@app.route('/')
def root():
    return ht

@app.route('/stream')
def stream():
    def eventStream():
        last_change = ""
        num = 0
        while True:
            # if open("index.js", encoding="utf-8").read() != last_change:
            #     last_change = open("index.js", encoding="utf-8").read()
            #     yield 'data: {}\n\n'.format(last_change)
            #     # yield last_change
            # print('data: {}\n\n'.format(get_message()))
            # yield 'data: {}\n\n'.format(get_message())
            num = num + 1
            yield 'data: {}\n\n'.format(f"Hola {num}")
            time.sleep(1)
    return Response(eventStream(), mimetype="text/event-stream")


app.run(port=8345)