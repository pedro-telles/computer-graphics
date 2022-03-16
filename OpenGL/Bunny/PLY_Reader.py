from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

class PLYReader:

    def __init__ (self, file):
        self.dir = file

    def _is_end_of_header(self, line):
        return line == 'end_header'

    def _is_ply_file(self, lines):
        return lines[0] == 'ply'

    def _extract_header_information(self, line, dict):
        words = line.split(' ')
        if words[0] == 'comment':
            key = words[0]
            if key not in dict.keys():
                dict[key] = [' '.join(words[1::])]
            else:
                dict[key].append(' '.join(words[1::]))

        if words[0] == 'element' and words[1] in ['vertex', 'face']:
            key = '_'.join(words[:2:])
            dict[key] = int(words[2])
        
        if words[0] == 'property':
            if 'element_face' not in dict.keys():
                key = 'vertex_' + words[0]
                if key not in dict.keys():
                    dict[key] = {
                        'description': [words[2]],
                        'type': [words[1]]
                    }
                else:
                    dict[key]['description'].append(words[2])
                    dict[key]['type'].append(words[2])
        
            else:
                key = 'face_' + words[0]
                if key not in dict.keys():
                    dict[key] = {
                        'description': [words[2::]],
                        'type': [words[1]]
                    }
                else:
                    dict[key]['description'].append(words[2::])
                    dict[key]['type'].append(words[2])
        
    def extract_data(self):
        ply_object = open(self.dir, 'r', encoding="utf-8", errors='ignore')
        
        lines = ply_object.read().splitlines() 
        
        header = self._get_header(lines)
        data = self._get_data(lines, header)
        
        return header, data

    def _get_data(self, lines, header):
        header_size = header['element_header']
        vertex_size = header['element_vertex']
        face_size = header['element_face']

        data = {
            'vertex': [],
            'face':[]
        }

        for line in lines[header_size:(vertex_size + header_size):]:
            data['vertex'].append(line)
        
        for line in lines[(vertex_size + header_size + 1)::]:
            data['face'].append(line)

        return data

    def _get_header(self, lines):
        
        header = {}
        header_size = 0
        if self._is_ply_file(lines):
            header_size += 1

            for line in lines[1::]:
                header_size += 1
                if self._is_end_of_header(line):
                    break
                self._extract_header_information(line, header)

            header['element_header'] = header_size
            return header

        else:
            raise Exception('O arquivo deve seguir o formato ply')


converter_helpper = {
    'float': lambda x: float(x),
    'int': lambda x: int(x)
}