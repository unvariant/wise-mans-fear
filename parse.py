def parse (line: str):
    parts = list(map(lambda s: s.strip(), [line[:line.find(":")], line[line.find(":")+1:]]));
    path = parts[0][parts[0].rfind("/")+1:];
    prompt = parts[1][parts[1].find("\"")+1:parts[1].rfind("\"")]; 

    return (path, prompt);

def object (prefix: str, prompt: str, path: str):
    return "{\"path\":\"" + path + "\",\"prefix\":\"" + prefix + "\",\"prompt\":\"" + prompt + "\"}"

f = open("dream_log.txt");
lines = map(lambda s: s.strip(), f.readlines());
f.close();

chapter_number = 1

json = []

parts = parse(next(lines))
json.append(object("Book", parts[1], parts[0]));
parts = parse(next(lines))
json.append(object("Prolouge", parts[1], parts[0]));

lines = list(lines);

for i in range(len(lines) - 1):
    parts = parse(lines[i]);
    path = parts[0];
    prompt = parts[1];

    prompt = prompt.replace("Interlude:", "Interlude — ");
    obj = object(f"Chapter {i + 1}", prompt, path);

    json.append(obj);

parts = parse(lines[-1])
json.append(object("Epilouge", parts[1], parts[0]));

out = open("images.json", "w");
out.write("[" + ",".join(json) + "]");
out.close();