import OpenGL.GL.shaders
from pyglet.gl import *
import ctypes
from array import array


class Triangle:
    def __init__(self):
        self.triangle = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                          0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                          0.0,  0.5, 0.0, 0.0, 0.0, 1.0]

        self.vertex_shader_source = """
        #version 120
        attribute vec3 position;
        attribute vec3 color;
        varying vec3 newColor;
        
        void main() {
            gl_Position = vec4(position, 1.0f);
            newColor = color;
        }
        """

        self.fragment_shader_source = """
        #version 120
        varying vec3 newColor;
        
        void main() {
            gl_FragColor = vec4(newColor, 1.0f);
        }
        """

        vertexShader = OpenGL.GL.shaders.compileShader(self.vertex_shader_source, GL_VERTEX_SHADER)
        fragmentShader = OpenGL.GL.shaders.compileShader(self.fragment_shader_source, GL_FRAGMENT_SHADER)
        shader = glCreateProgram()
        glAttachShader(shader, vertexShader)
        glAttachShader(shader, fragmentShader)
        glBindAttribLocation(shader, 0, b"position")
        glBindAttribLocation(shader, 1, b"color")
        # glBindAttribLocation(shader, 2, b"newcolor")
        # glBindAttribLocation(shader, 2, "vTexcoord")
        glLinkProgram(shader)

        # shader = OpenGL.GL.shaders.compileProgram(
        #     OpenGL.GL.shaders.compileShader(self.vertex_shader_source, GL_VERTEX_SHADER),
        #     OpenGL.GL.shaders.compileShader(self.fragment_shader_source, GL_FRAGMENT_SHADER)
        # )

        glUseProgram(shader)

        vbo = GLuint(0)
        glGenBuffers(1, vbo)

        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, 6*3*4, array('f',self.triangle).tostring(), GL_STATIC_DRAW)

        #positions
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6*4, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        #colors
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6*4, ctypes.c_void_p(3*4))
        glEnableVertexAttribArray(1)
