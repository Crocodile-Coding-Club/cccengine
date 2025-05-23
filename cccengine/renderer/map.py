import json
import math
from cccengine.renderer.chunk import Chunk

class Map:
    def __init__(self, file):
        self.file: dict = self.loadFile(file)
        self.width: int = self.file["width"]
        self.height: int = self.file["height"]
        
        self.chunk_x = None
        self.chunk_y = None
        
        self.textures = []
        texture_file: dict = self.file["tiles_type"]
        for path in texture_file.values():
            self.textures.append(path)

        self.chunk_dict: dict = self.readMap(self.file["chunks"])
        self.chunks:list[Chunk] = []

    def loadFile(self, file):
        with open(file, 'r') as f:
            data = json.load(f)
        return data
    
    def readMap(self, chunks):
        chunk_dict: dict = {}
        print(chunks)
        for chunk_name, chunk in chunks.items():
            chunk_name: str = chunk_name.split("#")
            chunk_dict[(int(chunk_name[1]), int(chunk_name[2]))] = Chunk(int(chunk_name[1]), int(chunk_name[2]), chunk, self.textures)
        return chunk_dict
    
    def loadChunks(self, chunk_x, chunk_y):
        if self.chunk_x != chunk_x or self.chunk_y != chunk_y:
            self.chunk_x = chunk_x
            self.chunk_y = chunk_y

            self.chunks = []

            for i in range(chunk_x-1, chunk_x+2):
                for j in range(chunk_y-1, chunk_y+2):
                    if self.chunk_dict.get((i, j)) is not None:
                        self.chunks.append(self.chunk_dict.get((i, j)))
    
    def update(self, x, y):
        for chunk in self.chunks:
            chunk.update(x, y)

    def draw(self, screen):
        for chunk in self.chunks:
            chunk.draw(screen)