with open("models/Cube.obj") as f:

    vertices = []
    faces = []

    for line in f:
        line = line.strip()

        if line[0] == "v":
            x = line.split()[1:]
            x = [float(i) for i in x]
            vertices.append(x)

        if line[0] == "f":
            x = line.split()[1:]
            x = [int(i) - 1 for i in x]
            faces.append(x)

    print("vertices: ", vertices)
    # print("faces: ", faces)

    edges = set()

    for face in faces:
        for i in range(len(face)):
            edge = tuple(sorted((face[i - 1], face[i])))
            edges.add(edge)

    edges = list(edges)

    print(f"found {len(edges)} edges")
    print(edges)
