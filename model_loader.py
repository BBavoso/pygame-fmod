def load_model(
    object_file_path: str,
) -> tuple[list[list[float]], list[tuple[int, int]]]:
    with open(object_file_path) as f:

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

        edges = set()

        for face in faces:
            for i in range(len(face)):
                edge = tuple(sorted((face[i - 1], face[i])))
                edges.add(edge)

        edges = list(edges)

        # print(
        #     f"found {len(vertices)} vertices, {len(faces)} faces and {len(edges)} edges"
        # )

        return (vertices, edges)
