from manim import *

class Thumbnail(Scene):
    def construct(self):

        gleichung = Tex(".Maxwell-Gleichungen.").scale(2).set_z_index(1)
        gleichung[0][0].set_opacity(0)
        gleichung[0][-1].set_opacity(0)
        b1 = SurroundingRectangle(gleichung,color=BLACK, fill_color=BLACK ,fill_opacity=0.9, stroke_width=0, corner_radius=0.6).set_z_index(1)

        #Bfield
        stream1 = SVGMobject("Magnetfield.svg", use_svg_cache=False).set_fill(opacity=0).scale(6).set_z_index(-1)
        center = stream1.get_center() 
        paths = stream1.family_members_with_points()
        distances = [np.linalg.norm(path.get_center() - center) for path in paths]
        max_distance = max(distances)
        for path, dist in zip(paths, distances):
            t = dist / max_distance  # 0 = center, 1 = farthest
            color = color_gradient([BLUE, RED, BLACK], 100)[int(t*99)]
            path.set_stroke(color=color, width=2)
        stream1 = VGroup(*paths).set_z_index(-1)     

        self.add(b1,gleichung)
        self.add(stream1)

class Opening(Scene):
    def construct(self):
        
        gleichung = Tex(".Maxwell-Gleichungen.").scale(2).set_z_index(1)
        gleichung[0][0].set_opacity(0)
        gleichung[0][-1].set_opacity(0)
        b1 = SurroundingRectangle(gleichung,color=BLACK, fill_color=BLACK ,fill_opacity=0.9, stroke_width=0, corner_radius=0.6).set_z_index(1)

        #Bfield
        stream1 = SVGMobject("Magnetfield.svg", use_svg_cache=False).set_fill(opacity=0).scale(6).set_z_index(-1)
        center = stream1.get_center() 
        paths = stream1.family_members_with_points()
        distances = [np.linalg.norm(path.get_center() - center) for path in paths]
        max_distance = max(distances)
        for path, dist in zip(paths, distances):
            t = dist / max_distance  # 0 = center, 1 = farthest
            color = color_gradient([BLUE, RED, BLACK], 100)[int(t*99)]
            path.set_stroke(color=color, width=2)
        stream1 = VGroup(*paths).set_z_index(-1)

        stream2 = SVGMobject("Magnetfield.svg").set_fill(opacity=0).scale(5).set_z_index(-3)
        center = stream2.get_center() 
        paths = stream2.family_members_with_points()
        distances = [np.linalg.norm(path.get_center() - center) for path in paths]
        max_distance = max(distances)
        for path, dist in zip(paths, distances):
            t = dist / max_distance  # 0 = center, 1 = farthest
            color = color_gradient([BLUE, RED, BLACK], 100)[int(t*99)]
            path.set_stroke(color=color, width=1)
        stream2 = VGroup(*paths).set_z_index(-3)

        stream3 = SVGMobject("Magnetfield.svg").set_fill(opacity=0).scale(5).set_z_index(-3)
        center = stream3.get_center() 
        paths = stream3.family_members_with_points()
        distances = [np.linalg.norm(path.get_center() - center) for path in paths]
        max_distance = max(distances)
        for path, dist in zip(paths, distances):
            t = dist / max_distance  # 0 = center, 1 = farthest
            color = color_gradient([BLUE, RED, BLACK], 100)[int(t*99)]
            path.set_stroke(color=color, width=1)
        stream3 = VGroup(*paths).set_z_index(-3)

        stream4 = SVGMobject("Magnetfield.svg").set_fill(opacity=0).scale(10).set_z_index(-3)
        center = stream4.get_center() 
        paths = stream4.family_members_with_points()
        distances = [np.linalg.norm(path.get_center() - center) for path in paths]
        max_distance = max(distances)
        for path, dist in zip(paths, distances):
            t = dist / max_distance  # 0 = center, 1 = farthest
            color = color_gradient([BLUE, RED, BLACK], 100)[int(t*99)]
            path.set_stroke(color=color, width=2)
        stream4 = VGroup(*paths).set_z_index(-3).shift(DOWN*0.4 + RIGHT*0.2)

        north_pole1 = Rectangle(width=1,height=0.5,color=BLUE,fill_opacity=1).shift(LEFT*0.5)
        south_pole1 = Rectangle(width=1,height=0.5,color=RED,fill_opacity=1).shift(LEFT*-0.5)
        north_pole_tex1 = MathTex(r"N").move_to(north_pole1)
        south_pole_tex1 = MathTex(r"S").move_to(south_pole1)
        magnet1 = VGroup(north_pole1,south_pole1,north_pole_tex1,south_pole_tex1, stream2).move_to([-12,0,0])

        north_pole2 = Rectangle(width=1,height=0.5,color=BLUE,fill_opacity=1).shift(LEFT*0.5)
        south_pole2 = Rectangle(width=1,height=0.5,color=RED,fill_opacity=1).shift(LEFT*-0.5)
        north_pole_tex2 = MathTex(r"N").move_to(north_pole2)
        south_pole_tex2 = MathTex(r"S").move_to(south_pole2)
        magnet2 = VGroup(north_pole2,south_pole2,north_pole_tex2,south_pole_tex2, stream3).move_to([12,0,0]).set_z_index(-2)


        ##
        self.add_sound("Opening.wav", time_offset=1)
        self.add(b1,gleichung)
        self.add(stream1)
        
        self.wait()
        self.wait(4.4)
        self.play(VGroup(stream1,b1,gleichung).animate.scale(0.5), run_time=2.5)
        self.play(magnet1.animate.move_to([-3.1,0,0]), magnet2.animate.move_to([3.1,0,0]), rate_func=linear, run_time=5.5)
        shearIn = [[0, 0], [0, 1]]
        self.play(magnet1.animate.move_to([-1,0,0]), magnet2.animate.move_to([1,0,0]), VGroup(b1, gleichung).animate.apply_matrix(shearIn), stream1.animate.apply_matrix(shearIn), FocusOn(gleichung), rate_func=linear, run_time=5.5/4.2381)

        self.remove(gleichung,stream1,b1)
        magnet1[1].set_color(BLUE)
        magnet2[0].set_color(RED)
        self.remove(magnet1[3],magnet2[2])

        # particles
        class Electron(VGroup):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                core = Circle(radius=0.4,color=PURE_GREEN,fill_color=PURE_GREEN,fill_opacity=1)
                corss = Rectangle(height=0.03,width=0.3,fill_opacity=1)
                self.core = core
                self.cross = corss
                self.add(core, corss)
 
        class Proton(VGroup):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                core = Circle(radius=0.4,color=RED,fill_opacity=1)
                corss1 = Rectangle(height=0.02,width=0.4,fill_opacity=1)
                corss2 = Rectangle(height=0.4,width=0.02,fill_opacity=1)
                self.add(VGroup(core,corss1,corss2))


        t = ValueTracker(0)

        electron1 = Electron()
        electron2 = Electron()
        electron3 = Electron()
        electron4 = Electron()
        proton1 = Proton()
        proton2 = Proton()
        proton3 = Proton()
        proton4 = Proton()
        self.add(electron1,electron2,electron3,electron4)
        self.add(proton1,proton2,proton3,proton4)

        f = 3
        electron1.add_updater(lambda mob: mob.move_to([-1*f*np.cos(t.get_value())+1*f, -1*f*np.sin(t.get_value()), 0]))
        electron2.add_updater(lambda mob: mob.move_to([-0.125*f*np.cos(t.get_value())+0.125*f, -0.5*f*np.sin(t.get_value()), 0]))
        electron3.add_updater(lambda mob: mob.move_to([0.125*f*np.cos(t.get_value())-0.125*f, 0.5*f*np.sin(t.get_value()), 0]))
        electron4.add_updater(lambda mob: mob.move_to([1*f*np.cos(t.get_value())-1*f, 1*f*np.sin(t.get_value()), 0]))
        proton1.add_updater(lambda mob: mob.move_to([1*f*np.cos(t.get_value())-1*f, -1*f*np.sin(t.get_value()), 0]))
        proton2.add_updater(lambda mob: mob.move_to([0.125*f*np.cos(t.get_value())-0.125*f, -0.5*f*np.sin(t.get_value()), 0]))
        proton3.add_updater(lambda mob: mob.move_to([-0.125*f*np.cos(t.get_value())+0.125*f, 0.5*f*np.sin(t.get_value()), 0]))
        proton4.add_updater(lambda mob: mob.move_to([-1*f*np.cos(t.get_value())+1*f, 1*f*np.sin(t.get_value()), 0]))
        self.play(FadeOut(VGroup(stream2,stream3)), FadeIn(stream4), t.animate.set_value(0.4), Flash([0,0,0], line_length=2), rate_func=linear, run_time=1)
        self.play(t.animate.set_value(2), rate_func=linear, run_time=4)

        electron1.clear_updaters()
        electron2.clear_updaters()
        electron3.clear_updaters()
        electron4.clear_updaters()
        proton1.clear_updaters()
        proton2.clear_updaters()
        proton3.clear_updaters()
        proton4.clear_updaters()

        lefover = VGroup(magnet1[0:4],magnet2[0:4], stream4,electron4,electron2,electron3,proton1,proton2,proton3,proton4)
        south_pole_tex1.set_z_index(-10)
        north_pole_tex2.set_z_index(-10)
        
        self.play(lefover.animate.rotate(-83*DEGREES, about_point=[13,0,0]), Rotate(electron1, 2*PI), run_time=3)
        self.remove(lefover)

        axis = Axes(x_range=[-20,0], y_range=[-1,1], x_length=20, y_length=2)
        b9 = SurroundingRectangle(axis,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0).set_z_index(1)
        VGroup(axis,b9).rotate(-20*DEGREES).shift(LEFT*5+ UP*0.6)
        axis.set_opacity(0)
        graph1 = axis.plot(lambda x: 0)
        graph2 = axis.plot(lambda x: 0)

        t2 = ValueTracker(0)
        b = 2
        c = 2
        graph1.add_updater(lambda mob: mob.become(axis.plot(lambda x: np.sin(x+t2.get_value()) * 1/(1+np.pow(c*2.71828, b*x +1.5)),color=BLUE).set_z_index(-2)))
        graph2.add_updater(lambda mob: mob.become(axis.plot(lambda x: -0.5*np.sin(x+t2.get_value()) * 1/(1+np.pow(c*2.71828, b*x +1.5)), color=YELLOW).set_z_index(-2)))


        self.add(graph1,graph2, b9)
        electron1.set_z_index(2)
        self.play(b9.animate.set_opacity(0), t2.animate.set_value(2), rate_func=linear, run_time=1)
        self.play(t2.animate.set_value(14), rate_func=linear, run_time=4)
        self.play(b9.animate.set_opacity(1), t2.animate.set_value(16), rate_func=linear, run_time=1)

        #positron
        class Positron(VGroup):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                core = Circle(radius=0.4,color=PURE_RED,fill_color=PURE_RED,fill_opacity=1)
                corss = Rectangle(height=0.03,width=0.3,fill_opacity=1)
                self.core = core
                self.cross = corss
                self.add(core, corss)

        pos1 = Positron().move_to([-5,5,0])
        self.remove(graph1,graph2, b9)
        self.play(pos1.animate.move_to([0,0,0]),electron1.animate.move_to([0,0,0]), rate_func=rate_functions.ease_in_quad, run_time=5)
        self.play(FadeOut(VGroup(electron1,pos1)),  Flash([0,0,0], line_length=2))
        self.wait()

class Overview(Scene):
    def construct(self):   

        header = Tex("Maxwell-Gleichungen")
        maxwell = ImageMobject("maxwell.jpg")
        first = Tex("1.").shift(UP*2.3).to_edge(LEFT)
        second = Tex("2.").shift(UP*1).to_edge(LEFT)
        third = Tex("3.").shift(UP*-1).to_edge(LEFT)
        forth = Tex("4.").shift(UP*-3).to_edge(LEFT)

        equation1 = MathTex(r" \nabla \cdot \vec{E} = \frac{\rho }{\varepsilon _{0}}").shift(UP*2.3).next_to(first,RIGHT)
        equation2 = MathTex(r" \nabla \cdot \vec{B} = 0").shift(UP*1).next_to(second,RIGHT)
        equation3 = MathTex(r" \nabla \times \vec{E}=-\frac{\partial \vec{B}}{\partial t}").shift(UP*-1).next_to(third,RIGHT)
        equation4 = MathTex(r" \nabla \times \vec{B}=\mu_{0}(\vec{J}+\varepsilon _{0}\frac{\partial \vec{E}}{\partial t})").shift(UP*-3).next_to(forth,RIGHT)

        #overview
        self.add_sound("Overview.wav", time_offset=1)

        self.play(Write(header))
        self.play(header.animate.to_edge(UP))
        self.play(FadeIn(maxwell))
        self.play(maxwell.animate.shift(RIGHT*4))
        self.play(FadeIn(VGroup(first,equation1)))
        self.wait()
        self.play(FadeIn(VGroup(second,equation2)))
        self.wait()
        self.play(FadeIn(VGroup(third,equation3)))
        self.wait()
        self.play(FadeIn(VGroup(forth,equation4)))
        self.wait(6)

        #short look at 1
        self.play(FadeOut(maxwell))
        self.play(VGroup(second,third,forth,equation2,equation3,equation4).animate.set_opacity(0.4), VGroup(first,equation1).animate.scale(1.2).to_edge(LEFT))

        func1 = lambda pos: 3*(pos[0]/(pos[0]**2 + pos[1]**2 +0.0001)) * RIGHT + 3*(pos[1]/(pos[0]**2 + pos[1]**2 +0.0001)) * UP
        vector_field = ArrowVectorField(func1,x_range=[-3,3],y_range=[-2.5,2.5]).move_to([3.5,-0.5,0])

        core = Circle(radius=0.4,color=RED,fill_opacity=1)
        corss1 = Rectangle(height=0.02,width=0.4,fill_opacity=1)
        corss2 = Rectangle(height=0.4,width=0.02,fill_opacity=1)
        proton = VGroup(core,corss1,corss2).scale(0.8).move_to([3.5,-0.5,0])

        b1 = SurroundingRectangle(vector_field,color=WHITE)

        self.play(FadeIn(b1))
        self.play(FadeIn(proton))
        self.play(FadeIn(vector_field))
        self.wait(6)

        self.play(FadeOut(VGroup(proton,vector_field)))
        self.wait()


        # short look at 2
        self.play(VGroup(first,equation1).animate.set_opacity(0.4).scale(1/1.2).to_edge(LEFT), VGroup(second,equation2).animate.scale(1.2).to_edge(LEFT).set_opacity(1))
        
        func1 = lambda pos: vecField1(pos=pos)
        def vecField1(pos):
            e = 0.001
            s = 0.2
            x = pos[0]
            y = pos[1]
            normal1 = x**2 + (y-s)**2 + e
            normal2 = x**2 + (y+s)**2 + e
            field = [0,0]
            field[0] = (y-s)/(normal1) - (y+s)/(normal2)
            field[1] = (-x)/(normal1) + (x)/(normal2)
            return field[0]*RIGHT + field[1]*UP

        vector_field1 = ArrowVectorField(func=func1,max_color_scheme_value=0.1,min_color_scheme_value=0.01,x_range=[-3,3],y_range=[-2.5,2.5]).move_to([3.5,-0.5,0])

        north_pole = Rectangle(width=1,height=0.5,color=BLUE,fill_opacity=1).shift(LEFT*0.5)
        south_pole = Rectangle(width=1,height=0.5,color=RED,fill_opacity=1).shift(LEFT*-0.5)
        north_pole_tex = MathTex(r"N").move_to(north_pole)
        south_pole_tex = MathTex(r"S").move_to(south_pole)
        magnet = VGroup(north_pole,south_pole,north_pole_tex,south_pole_tex).move_to([3.5,-0.5,0]).set_z_index(1)

        self.play(FadeIn(VGroup(magnet,vector_field1)))
        self.wait(7)

class Preview(ThreeDScene):
    def construct(self):   

        #first law demo
        def vecField1(pos):
            e = 0.5
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = (x+2)/((x+2)**2 + y**2 + e) - (x-2)/((x-2)**2 + y**2 + e)
            field[1] = y/((x+2)**2 + y**2 + e) - y/((x-2)**2 + y**2 + e)
            return field[0]*RIGHT + field[1]*UP

        colors1 = [BLUE, YELLOW]
        vecField1Func1 = lambda pos: vecField1(pos=pos)
        stream = StreamLines(vecField1Func1, stroke_width=2, max_anchors_per_line=100, virtual_time=5, n_repeats=4, max_color_scheme_value=2, min_color_scheme_value=0.01, color=colors1).set_z_index(-1)
        
        core = Circle(radius=0.4,color=RED,fill_opacity=1)
        corss1 = Rectangle(height=0.02,width=0.4,fill_opacity=1)
        corss2 = Rectangle(height=0.4,width=0.02,fill_opacity=1)
        proton = VGroup(core,corss1,corss2).shift(LEFT*2).scale(0.7)

        core1 = Circle(radius=0.4,color=PURE_GREEN,fill_color=PURE_GREEN,fill_opacity=1)
        corss3 = Rectangle(height=0.03,width=0.3,fill_opacity=1)
        electron = VGroup(core1,corss3).shift(RIGHT*2).scale(0.7)

        #start
        self.add_sound("Preview.wav", time_offset=1)
        self.wait()
        self.play(FadeIn(VGroup(proton, electron)), run_time=0.5)
        self.add(stream)
        stream.start_animation(flow_speed=1.4, warm_up=True)
        self.wait(7)
        self.remove(stream,proton,electron)


        #forth law demo
        def vecField2(pos):
            r = 0.03
            b = 1
            e = 0.01
            x = pos[0]
            y = pos[1]
            norm = x**2 + y**2 + e
            field = [0,0]
            field[0] = -b*y/norm
            field[1] = b*x/norm
            if field[0]**2 + field[1]**2 < r:
                return 0*RIGHT + 0*UP
            else:
                return field[0]*RIGHT + field[1]*UP

        pipe2 = Cylinder(radius=0.5, height=6, resolution=[1,10], v_range=[0,PI])
        func2 = lambda pos: RIGHT
        stream2 = StreamLines(func2, stroke_width=4, max_anchors_per_line=25, virtual_time=1, n_repeats=1,
                             y_range=[-0.2,0.2], x_range=[-2.2,2.2]).rotate(PI/2,OUT).rotate(PI/2,RIGHT).move_to(pipe2)
        colors2 = [BLUE, YELLOW, YELLOW, ORANGE, ORANGE, RED]
        vecField1Func2 = lambda pos: vecField2(pos=pos)
        vector_field2 = ArrowVectorField(vecField1Func2, max_color_scheme_value=0.8, min_color_scheme_value=0.2, colors=colors2, x_range=[-6,6], y_range=[-6,6])

        #start
        self.add(pipe2,stream2, vector_field2)
        stream2.start_animation(warm_up=False, flow_speed=1)
        self.move_camera(phi=60*DEGREES, run_time=1)
        self.begin_ambient_camera_rotation(0.1)
        self.wait(7)
        self.stop_ambient_camera_rotation()
        self.remove(stream2,pipe2,vector_field2)


        #second law demo
        def vecField3(pos):
            e = 0.001
            s = 0.2
            x = pos[0]
            y = pos[1]
            normal1 = x**2 + (y-s)**2 + e
            normal2 = x**2 + (y+s)**2 + e
            field = [0,0]
            field[0] = (y-s)/(normal1) - (y+s)/(normal2)
            field[1] = (-x)/(normal1) + (x)/(normal2)
            return 3*field[0]*RIGHT + 3*field[1]*UP

        north_pole3 = Rectangle(width=1,height=0.5,color=BLUE,fill_opacity=1).shift(LEFT*0.5)
        south_pole3 = Rectangle(width=1,height=0.5,color=RED,fill_opacity=1).shift(LEFT*-0.5)
        north_pole_tex3 = MathTex(r"N").move_to(north_pole3)
        south_pole_tex3 = MathTex(r"S").move_to(south_pole3)
        magnet3 = VGroup(north_pole3,south_pole3,north_pole_tex3,south_pole_tex3).move_to([0,0,0.1]).set_z_index(1)

        func3 = lambda pos: vecField3(pos=pos)
        stream3 = StreamLines(func3, stroke_width=2, max_anchors_per_line=200, virtual_time=20, n_repeats=5).set_z_index(-1)

        self.add_fixed_in_frame_mobjects(magnet3)
        self.play(FadeIn(magnet3))
        self.move_camera(phi=0, theta=-PI/2, run_time=0.01)
        self.add(stream3)
        stream3.start_animation(warm_up=True, flow_speed=3)
        self.wait(7)
        self.remove(magnet3,stream3)

        #third law demo
        func4 = lambda pos: vecField4(pos=pos)
        def vecField4(pos):
            e = 0.001
            s = 0.2
            x = pos[0]
            y = pos[1]
            normal1 = x**2 + (y-s)**2 + e
            normal2 = x**2 + (y+s)**2 + e
            field = [0,0]
            field[0] = (y-s)/(normal1) - (y+s)/(normal2)
            field[1] = (-x)/(normal1) + (x)/(normal2)
            return field[0]*RIGHT + field[1]*UP

        def currentFlow4(x, b=1, c=10):
            return -(c * x) / ((x**2 + b**2)**2)

        #setup
        north_pole4 = Prism(dimensions=[2,1,1], fill_color=BLUE, fill_opacity=1).move_to([1,0,0])
        south_pole4 = Prism(dimensions=[2,1,1], fill_color=RED, fill_opacity=1).move_to([-1,0,0])

        #Bfield
        stream4 = SVGMobject("Magnetfield.svg").set_fill(opacity=0).set_stroke(PURE_GREEN, width=0.5, opacity=0.9).scale(8)
        center = stream4.get_center() 
        paths = stream4.family_members_with_points()
        distances = [np.linalg.norm(path.get_center() - center) for path in paths]
        max_distance = max(distances)
        for path, dist in zip(paths, distances):
            t = dist / max_distance  # 0 = center, 1 = farthest
            color = color_gradient([BLUE, RED, BLACK], 100)[int(t*99)]
            path.set_stroke(color=color, width=0.7)
        stream4 = VGroup(*paths)

        magnet4 = VGroup(stream4, south_pole4, north_pole4)


        loop = Circle(radius=2,color=GREEN).rotate(PI/2,UP) 
        #move magnet
        vec1 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,0,2]).rotate(PI/2,OUT)
        vec2 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,2,0]).rotate(PI/2,UP)
        vec3 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,0,-2]).rotate(-PI/2,OUT)
        vec4 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,-2,0]).rotate(-PI/2,UP)
        l1 = Line(start=[0,0,2], end=[0,0,2], color=YELLOW)
        l2 = Line(start=[0,2,0], end=[0,2,0], color=YELLOW)
        l3 = Line(start=[0,0,-2], end=[0,0,-2], color=YELLOW)
        l4 = Line(start=[0,-2,0], end=[0,-2,0], color=YELLOW)
        vec1.add_updater(lambda mob: mob.set_y(currentFlow4(magnet4.get_x())))
        vec2.add_updater(lambda mob: mob.set_z(-currentFlow4(magnet4.get_x())))
        vec3.add_updater(lambda mob: mob.set_y(-currentFlow4(magnet4.get_x())))
        vec4.add_updater(lambda mob: mob.set_z(currentFlow4(magnet4.get_x())))
        l1.add_updater(lambda mob: mob.become(Line(start=[0,0,2], end=vec1.get_center(), color=YELLOW)))
        l2.add_updater(lambda mob: mob.become(Line(start=[0,2,0], end=vec2.get_center(), color=YELLOW)))
        l3.add_updater(lambda mob: mob.become(Line(start=[0,0,-2], end=vec3.get_center(), color=YELLOW)))
        l4.add_updater(lambda mob: mob.become(Line(start=[0,-2,0], end=vec4.get_center(), color=YELLOW)))
        vecs = VGroup(vec1,vec2,vec3,vec4, l1,l2,l3,l4)

        magnet4.move_to([-4,0,0])
        self.add(stream4)

        self.add(magnet4,vecs, loop)
        self.move_camera(phi=60*DEGREES, theta=-45*DEGREES, run_time=1)
        self.play(magnet4.animate.move_to([4,0,0]), rate_func=linear, run_time=5)
        self.play(magnet4.animate.move_to([-4,0,0]), rate_func=linear, run_time=5)
        self.remove(magnet4,vecs, loop)
        self.wait()

class MagnetIntro(Scene):
    def construct(self):
        
        func1 = lambda pos: vecField1(pos=pos)
        def vecField1(pos):
            e = 0.001
            s = 0.2
            x = pos[0]
            y = pos[1]
            normal1 = x**2 + (y-s)**2 + e
            normal2 = x**2 + (y+s)**2 + e
            field = [0,0]
            field[0] = (y-s)/(normal1) - (y+s)/(normal2)
            field[1] = (-x)/(normal1) + (x)/(normal2)
            return field[0]*RIGHT + field[1]*UP
        
        stream = StreamLines(func1, stroke_width=3, max_anchors_per_line=150, virtual_time=60, n_repeats=1).set_z_index(-1)

        north_pole = Rectangle(width=1,height=0.5,color=BLUE,fill_opacity=1).shift(LEFT*0.5)
        south_pole = Rectangle(width=1,height=0.5,color=RED,fill_opacity=1).shift(LEFT*-0.5)
        north_pole_tex = MathTex(r"N").move_to(north_pole)
        south_pole_tex = MathTex(r"S").move_to(south_pole)
        magnet = VGroup(north_pole,south_pole,north_pole_tex,south_pole_tex).move_to([0,0,0.1]).set_z_index(1)

        #magnet and fieldlines
        self.wait()
        self.play(Write(magnet), run_time=2)
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=5)
        self.wait(7)
        self.play(FadeOut(stream))
        stream.end_animation()
        self.remove(stream)

        #2small magnets
        north_pole2 = Rectangle(width=0.5,height=0.5,color=BLUE,fill_opacity=1).shift(LEFT*0.25)
        south_pole2 = Rectangle(width=0.5,height=0.5,color=RED,fill_opacity=1).shift(LEFT*-0.25)
        north_pole_tex2 = MathTex(r"N").move_to(north_pole2)
        south_pole_tex2 = MathTex(r"S").move_to(south_pole2)
        magnet2 = VGroup(north_pole2,south_pole2,north_pole_tex2,south_pole_tex2).move_to([-0.75,0,0.1]).set_z_index(1)
        north_pole3 = Rectangle(width=0.5,height=0.5,color=BLUE,fill_opacity=1).shift(LEFT*0.25)
        south_pole3 = Rectangle(width=0.5,height=0.5,color=RED,fill_opacity=1).shift(LEFT*-0.25)
        north_pole_tex3 = MathTex(r"N").move_to(north_pole3)
        south_pole_tex3 = MathTex(r"S").move_to(south_pole3)
        magnet3 = VGroup(north_pole3,south_pole3,north_pole_tex3,south_pole_tex3).move_to([0.75,0,0.1]).set_z_index(1)

        # self.add(NumberPlane())
        self.wait(3)
        self.play(ReplacementTransform(magnet,magnet2), ReplacementTransform(magnet.copy(),magnet3), run_time=2)
        self.wait(3)

        #keine monos
        mono = Tex("keine magnetischen Monopole").shift(UP*3)
        exept = Tex("*soweit wir wissen").shift(UP*2).scale(0.9).align_to(mono,LEFT)

        self.play(Write(mono))
        self.wait()
        self.play(FadeIn(exept))
        self.wait(5)
        self.play(FadeOut(exept))
        self.play(FadeOut(magnet3), magnet2.animate.move_to([0,0,0.1]))

        vector_field = ArrowVectorField(func=func1,max_color_scheme_value=0.1,min_color_scheme_value=0.01)
        self.wait(2)
        self.play(FadeIn(vector_field))
        self.wait()

class VectorIntro(Scene):
    def construct(self): 

        np = NumberPlane().set_opacity(0.5).set_color(BLUE).set_z_index(-1)
        xaxis = NumberLine(x_range=[-3,3,1], include_tip=True)
        yaxis = NumberLine(x_range=[-3,3,1], include_tip=True).rotate(PI/2)
        x = MathTex(r"x").next_to(xaxis,RIGHT)
        y = MathTex(r"y").next_to(yaxis,UP)
        p1 = Dot([3,2,0], color=YELLOW).scale(1.4)
        p1tex = MathTex(r"=(3,2)").next_to(p1,RIGHT,buff=0.5)
        p1tex2 = MathTex(r"=3x+2y").next_to(p1tex,DOWN).align_to(p1tex,LEFT)

        ihatvec = Vector(RIGHT,color=RED)
        jhatvec = Vector(UP,color=GREEN)

        #coords intro
        self.play(Write(xaxis))
        self.play(Write(x))
        self.play(Write(yaxis))
        self.play(Write(y))

        #intro point
        self.wait()
        self.play(Write(p1))
        self.play(Write(np))
        self.wait()


        #schreibweisen
        self.wait()
        self.play(Write(p1tex))
        self.wait(3)
        self.play(Write(p1tex2))

        #switch to basis vectors
        self.wait(3)
        self.play(Unwrite(p1tex),Unwrite(p1tex2), Unwrite(np))

        self.play(x.animate.set_color(RED))
        self.play(ReplacementTransform(xaxis,ihatvec), run_time=3)
        self.wait()
        self.play(x.animate.next_to(ihatvec,DOWN))
        self.wait()

        self.play(y.animate.set_color(GREEN))
        self.play(ReplacementTransform(yaxis,jhatvec))
        self.play(y.animate.next_to(jhatvec,LEFT))
        self.wait()

        #convert to vectors
        xvec = MathTex(r"\vec{x}").move_to(x)
        yvec = MathTex(r"\vec{y}").move_to(y)
        xvec[0][1].set_color(RED)
        yvec[0][1].set_color(GREEN)

        self.wait()
        self.play(Transform(x,xvec))
        self.wait()
        self.play(Transform(y,yvec))

        #linearity
        xvec2 = VGroup(ihatvec.copy(),x.copy()).shift(RIGHT)
        xvec3 = VGroup(ihatvec.copy(),x.copy()).shift(2*RIGHT)
        yvec1 = VGroup(jhatvec.copy(),y.copy()).shift(3*RIGHT)
        yvec2 = VGroup(jhatvec.copy(),y.copy()).shift(3*RIGHT+UP)

        self.wait(5)
        self.play(ReplacementTransform(ihatvec.copy(),xvec2), run_time=1.5)
        self.wait(0.5)
        self.play(ReplacementTransform(ihatvec.copy(),xvec3), run_time=1.5)
        self.wait(0.5)
        self.play(ReplacementTransform(jhatvec.copy(),yvec1), run_time=1.5)
        self.wait(0.5)
        self.play(ReplacementTransform(jhatvec.copy(),yvec2), run_time=1.5)
        self.wait()
        
        #combination
        np2 = NumberPlane().set_opacity(0.4).set_color(BLUE).set_z_index(-1)
        v = np2.get_vector([3,2,0],color=YELLOW)
        vtex = MathTex(r" \vec{v}").set_color(YELLOW).move_to(v).shift(LEFT*0.4+UP*0.4)

        self.wait()
        self.play(FadeIn(np2))
        self.wait()
        self.play(Write(v))
        self.wait()
        self.play(Unwrite(p1))
        self.wait(3)
        self.play(Write(vtex))
        
        vinxy = MathTex(r"\vec{v}",r"=3",r"\vec{x}",r"+2",r"\vec{y}").shift(DOWN*2)
        vinxy[0].set_color(YELLOW)
        vinxy[2][1].set_color(RED)
        vinxy[4][1].set_color(GREEN)
        self.wait(2)
        self.play(Write(vinxy), run_time=2)

        #transition i,j
        self.play(Unwrite(VGroup(xvec2,xvec3,yvec1,yvec2,p1tex,p1tex2,p1)))

        ihat = (MathTex(r"\hat{i}")).move_to(x).set_color(RED)
        jhat = (MathTex(r"\hat{j}")).move_to(y).set_color(GREEN)
        self.wait(3)
        self.play(ReplacementTransform(x,ihat))
        self.wait()
        self.play(ReplacementTransform(y,jhat))
        self.wait(6)

        vinij = MathTex(r"\vec{v}",r"=3",r"\hat{i}",r"+2",r"\hat{j}").shift(DOWN*2)
        vinij[0].set_color(YELLOW)
        vinij[2].set_color(RED)
        vinij[4].set_color(GREEN)
        self.play(ReplacementTransform(vinxy,vinij))
        self.wait()

class VectorFieldIntro(Scene):
    def construct(self):

        def vecField1(point: Dot):
            x = point.get_x()
            y = point.get_y()
            field = [0,0]
            field[0] = x
            field[1] = y
            return field
    

        #explain formula
        nump = NumberPlane().set_opacity(0.7)
        field_equation1 = MathTex(r"\vec{F}",r"(x,y)",r"=",r"x\hat{i} +y\hat{j}")
        point_example = Dot(color=PURE_GREEN).scale(1.6).next_to(field_equation1[1],UP)
        vector_example = Vector([2,1],color=YELLOW).next_to(field_equation1[3],UP)

        self.wait()
        self.play(Write(field_equation1))
        self.wait(2)
        self.play(Write(point_example))
        self.wait()

        self.play(Circumscribe(field_equation1[1],time_width=5),run_time=4)
        self.wait()
        self.play(Write(vector_example))
        self.wait()
        self.play(Circumscribe(field_equation1[3],time_width=5),run_time=4)
        self.wait()
        self.play(Unwrite(VGroup(point_example,vector_example)))

        self.play(field_equation1.animate.to_corner(UL).shift(UP*0.3))
        self.play(Write(nump))

        #point
        axis = Axes(x_length=12, y_length=7, x_range=[-1,1,10], y_range=[-1,1,10])
        x_label = MathTex(r"x").next_to(axis,RIGHT).shift(UP*0.5 + LEFT*0.6)
        y_label = MathTex(r"y").align_to(axis,UP).shift(RIGHT*0.5)
        labels = VGroup(x_label,y_label)

        p1 = Dot([0,0,0],color=PURE_GREEN).scale(1.6).set_z_index(1)

        field_equation1_example1 = MathTex(r"\vec{F}",r"(2,1)",r"=2\hat{i} +1\hat{j}").next_to(field_equation1,DOWN).to_edge(LEFT)
        field_equation1_example1[1][1].set_color(PURE_GREEN)
        field_equation1_example1[1][3].set_color(PURE_GREEN)
        field_equation1_example1[2][1].set_color(YELLOW)
        field_equation1_example1[2][5].set_color(YELLOW)

        self.wait()

        self.play(Write(axis),Write(labels))
        self.wait()
        self.play(Write(p1))
        self.wait()
        self.play(Write(field_equation1_example1[0:2]))
        self.wait(2)
        self.play(p1.animate.shift(RIGHT*2 + UP), run_time=2)

        #vector
        ihatvec = Vector(RIGHT,color=RED)
        jhatvec = Vector(UP,color=GREEN)
        ihat = (MathTex(r"\hat{i}")).next_to(ihatvec,DOWN).set_color(RED)
        jhat = (MathTex(r"\hat{j}")).next_to(jhatvec,LEFT).set_color(GREEN)
        vector1 = Vector([2,1],color=YELLOW).shift(RIGHT*2+UP)

        self.wait(2)
        self.play(Write(field_equation1_example1[2]))
        self.wait(3)

        self.play(Write(ihatvec),Write(ihat))
        self.play(Write(jhatvec),Write(jhat))
        self.wait(2)
        self.play(GrowArrow(vector1))


        #second position
        field_equation1_example2 = MathTex(r"\vec{F}",r"(-3,-1.5)",r"=-3\hat{i} -1.5\hat{j}").next_to(field_equation1,DOWN).to_edge(LEFT)
        field_equation1_example2[1][1:3].set_color(PURE_GREEN)
        field_equation1_example2[1][4:8].set_color(PURE_GREEN)
        field_equation1_example2[2][1:3].set_color(YELLOW)
        field_equation1_example2[2][5:9].set_color(YELLOW)

        vector1.add_updater(lambda mob: mob.become(Vector(vecField1(p1))).move_to(p1).shift(p1.get_center() - vector1.get_start()).set_color(YELLOW))

        self.wait(2)

        self.play(ReplacementTransform(field_equation1_example1,field_equation1_example2))
        self.wait()
        self.play(p1.animate.move_to([2,-1.5,0]), run_time=3)
        self.wait()
        self.play(p1.animate.move_to([-3,-1.5,0]), run_time=3)

        #prepare for full visual
        vector1.suspend_updating()
        self.wait()
        self.play(Unwrite(field_equation1_example2),Unwrite(p1),Unwrite(vector1))
        self.play(Unwrite(labels),Unwrite(axis))

        colors1 = [BLUE,GREEN,YELLOW,RED]
        vecField1Func1 = lambda pos: pos[0]*RIGHT + pos[1]*UP
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=6,min_color_scheme_value=1, colors=colors1)

        self.wait()
        self.play(Write(vector_field1))

        #streamlines
        stream = StreamLines(vecField1Func1, stroke_width=2, max_anchors_per_line=100, virtual_time=50, n_repeats=5, colors=colors1, min_color_scheme_value=1,  max_color_scheme_value=6)

        self.wait(6)

        self.play(vector_field1.animate.set_opacity(0.3), run_time=0.1)
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=5)
        self.wait(5)

class VectorFieldExamples1(Scene):
    def construct(self):

        def vecField2(point: Dot):
            x = point.get_x()
            y = point.get_y()
            field = [0,0]
            field[0] = y
            field[1] = 0
            return field

        colors1 = [BLUE,GREEN,YELLOW,RED]
        
        #prepare for full visual
        field_equation2 = MathTex(r"\vec{F}(x,y)=y\hat{i} +0\hat{j}").set_z_index(1)
        b1 = SurroundingRectangle(field_equation2,color=BLACK,fill_opacity=1,fill_color=BLACK).move_to(field_equation2).set_z_index(1)
        self.wait()
        self.play(Write(VGroup(b1,field_equation2)))
        self.wait(4)
        self.play(VGroup(b1,field_equation2).animate.to_corner(UL))

        vecField1Func2 = lambda pos: pos[1]*RIGHT + 0*pos[1]*UP
        vector_field2 = ArrowVectorField(vecField1Func2, max_color_scheme_value=3,min_color_scheme_value=0, colors=colors1).set_z_index(-1)
        self.play(Write(vector_field2))
        self.wait(10)

        #streamlines
        stream = StreamLines(vecField1Func2, stroke_width=2, max_anchors_per_line=100, virtual_time=50, n_repeats=5, colors=colors1, min_color_scheme_value=1,  max_color_scheme_value=3).set_z_index(-1)

        self.play(vector_field2.animate.set_opacity(0.3), run_time=1)
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=2)
        self.wait(7)

#DesmosField1

#DesmosField2

class VectorFieldExamples2(Scene):
    def construct(self):

        def vecField3(point: Dot):
            x = point.get_x()
            y = point.get_y()
            field = [0,0]
            field[0] = -y
            field[1] = x
            return field

        colors1 = [BLUE,GREEN,YELLOW,RED]
        
        #prepare for full visual
        field_equation3 = MathTex(r"\vec{F}(x,y)=-y\hat{i} +x\hat{j}").set_z_index(1)
        b1 = SurroundingRectangle(field_equation3,color=BLACK,fill_opacity=1,fill_color=BLACK).move_to(field_equation3).set_z_index(1)
        self.play(Write(VGroup(b1,field_equation3)))
        self.wait(4)
        self.play(VGroup(b1,field_equation3).animate.to_corner(UL))

        vecField1Func3 = lambda pos: -pos[1]*RIGHT + pos[0]*UP
        vector_field3 = ArrowVectorField(vecField1Func3, max_color_scheme_value=6,min_color_scheme_value=1, colors=colors1).set_z_index(-1)
        self.play(Write(vector_field3))

        #streamlines
        stream = StreamLines(vecField1Func3, stroke_width=2, max_anchors_per_line=50, virtual_time=50, n_repeats=1, colors=colors1, min_color_scheme_value=1,  max_color_scheme_value=6).set_z_index(-1)
        self.wait(7)

        self.play(vector_field3.animate.set_opacity(0.3), run_time=0.1)
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=2)
        self.wait(10)

class MagnetFieldPicture1(Scene):
    def construct(self):
        
        func1 = lambda pos: vecField1(pos=pos)
        def vecField1(pos):
            e = 0.0001
            s = 0.2
            x = pos[0]
            y = pos[1]
            normal1 = x**2 + (y-s)**2 + e
            normal2 = x**2 + (y+s)**2 + e
            field = [0,0]
            field[0] = (y-s)/(normal1) - (y+s)/(normal2)
            field[1] = (-x)/(normal1) + (x)/(normal2)
            return 3*field[0]*RIGHT + 3*field[1]*UP
        
        north_pole = Rectangle(width=1,height=0.5,color=BLUE,fill_opacity=1).shift(LEFT*0.5)
        south_pole = Rectangle(width=1,height=0.5,color=RED,fill_opacity=1).shift(LEFT*-0.5)
        north_pole_tex = MathTex(r"N").move_to(north_pole)
        south_pole_tex = MathTex(r"S").move_to(south_pole)
        magnet = VGroup(north_pole,south_pole,north_pole_tex,south_pole_tex).move_to([0,0,0.1]).set_z_index(1)
        vector_field = ArrowVectorField(func=func1,max_color_scheme_value=0.3,min_color_scheme_value=0.01)

        self.add(magnet,vector_field)

class MagnetFieldPicture2(Scene):
    def construct(self):
        
        func1 = lambda pos: vecField1(pos=pos)
        def vecField1(pos):
            e = 0.0001
            s = 0.2
            x = pos[0]
            y = pos[1]
            normal1 = x**2 + (y-s)**2 + e
            normal2 = x**2 + (y+s)**2 + e
            field = [0,0]
            field[0] = (y-s)/(normal1) - (y+s)/(normal2)
            field[1] = (-x)/(normal1) + (x)/(normal2)
            return 3*field[0]*RIGHT + 3*field[1]*UP
        
        north_pole = Rectangle(width=1,height=0.5,color=BLUE,fill_opacity=1).shift(LEFT*0.5)
        south_pole = Rectangle(width=1,height=0.5,color=GREEN,fill_opacity=1).shift(LEFT*-0.5)
        north_pole_tex = MathTex(r"N").move_to(north_pole)
        south_pole_tex = MathTex(r"S").move_to(south_pole)
        magnet = VGroup(north_pole,south_pole,north_pole_tex,south_pole_tex).move_to([0,0,0.1]).set_z_index(1)
        stream = StreamLines(func1, stroke_width=2, max_anchors_per_line=600, virtual_time=100, n_repeats=1, max_color_scheme_value=1.1, x_range=[-16,16], y_range=[-8,8]).set_z_index(-1).scale(0.5)

        self.add(magnet,stream)

class DivergenceExample1(Scene):
    def construct(self):

        def vecField1(pos):
            e = 0.5
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = (x+2)/((x+2)**2 + y**2 + e) - (x-2)/((x-2)**2 + y**2 + e)
            field[1] = y/((x+2)**2 + y**2 + e) - y/((x-2)**2 + y**2 + e)
            return field[0]*RIGHT + field[1]*UP

        def divFunc1(x,y,eps):
            xcomp = 1/((x+2)**2 + y**2 + eps)
            ycomp = 1/((x-2)**2 + y**2 + eps)
            return 2*eps*(xcomp - ycomp)

        colors1 = [BLUE, YELLOW]
        vecField1Func1 = lambda pos: vecField1(pos=pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=2,min_color_scheme_value=0.01, colors=colors1).set_z_index(-1)
        stream = StreamLines(vecField1Func1, stroke_width=2, max_anchors_per_line=100, virtual_time=5, n_repeats=4, max_color_scheme_value=2, min_color_scheme_value=0.01, color=colors1).set_z_index(-1)
        
        p1 = Dot().scale(0.5)
        c1 = Circle(color=WHITE,radius=0.2)
        div_tex = MathTex(r"div\vec{F}=")
        div_tex[0][3:5].set_color(YELLOW)
        decnum = DecimalNumber(0)
        s1 = SurroundingRectangle(div_tex,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)
        s2 = SurroundingRectangle(decnum,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)

        c1.add_updater(lambda mob: mob.move_to(p1))
        div_tex.add_updater(lambda mob: mob.next_to(p1,UP))
        s1.add_updater(lambda mob: mob.move_to(div_tex))
        s2.add_updater(lambda mob: mob.move_to(decnum))
        decnum.add_updater(lambda mob: mob.set_value(divFunc1(p1.get_x(),p1.get_y(),0.8)).next_to(p1,UP).shift(RIGHT*1.5))

        #fields
        self.play(Write(vector_field1))
        self.wait(6)
        self.add(stream)
        stream.start_animation(flow_speed=1.4)
        self.wait(3)

        rot = Tex("Divergenz").scale(1.5).to_edge(UP)
        b1 = SurroundingRectangle(rot,color=BLACK,fill_color=BLACK,fill_opacity=0.7, stroke_opacity=0).move_to(rot)
        self.play(FadeIn(VGroup(b1,rot)))
        self.wait(4)

        self.play(FadeIn(p1,s1,s2,decnum,c1,div_tex))
        self.wait(7)

        self.play(p1.animate.move_to([2,0,0]),run_time=3)
        self.wait(3)

        self.play(p1.animate.move_to([-2,0,0]),run_time=3)
        self.wait(2)
        self.play(p1.animate.move_to([-2,2,0]),run_time=3)
        self.wait()
        self.play(p1.animate.move_to([2,2,0]),run_time=3)
        self.wait()
        self.play(p1.animate.move_to([0,2,0]),run_time=3)
        self.wait()
        self.play(p1.animate.move_to([0,-2,0]),run_time=3)
        self.wait()
        self.play(p1.animate.move_to([0,0,0]),run_time=3)
        self.wait()

class DivergenceExample2(Scene):
    def construct(self):

        def vecField1(pos):
            e = 0.5
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = np.pow(2.7182, 0.6*x)
            field[1] = 0
            return field[0]*RIGHT + field[1]*UP

        colors1 = [BLUE, YELLOW, RED]
        vecField1Func1 = lambda pos: vecField1(pos=pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=1.2,min_color_scheme_value=0.0001, colors=colors1).set_z_index(-1)

        stream = StreamLines(vecField1Func1, stroke_width=2, max_anchors_per_line=50, virtual_time=10, n_repeats=5, max_color_scheme_value=1.1)

        
        p1 = Dot().scale(0.5)
        c1 = Circle(color=WHITE,radius=0.2)
        div_tex = MathTex(r"div\vec{F}>0")
        div_tex[0][3:5].set_color(YELLOW)
        s1 = SurroundingRectangle(div_tex,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)

        c1.add_updater(lambda mob: mob.move_to(p1))
        div_tex.add_updater(lambda mob: mob.next_to(c1,UP))
        s1.add_updater(lambda mob: mob.move_to(div_tex))

        #fields
        self.play(Write(vector_field1))
        self.wait(4)

        self.add(stream)
        stream.start_animation(flow_speed=1.5)
        self.wait(4)

        self.play(FadeIn(p1,s1,c1,div_tex))
        self.wait(13)

class MagnetRecap(Scene):
    def construct(self):
        
        func1 = lambda pos: vecField1(pos=pos)
        def vecField1(pos):
            e = 0.0001
            s = 0.2
            x = pos[0]
            y = pos[1]
            normal1 = x**2 + (y-s)**2 + e
            normal2 = x**2 + (y+s)**2 + e
            field = [0,0]
            field[0] = (y-s)/(normal1) - (y+s)/(normal2)
            field[1] = (-x)/(normal1) + (x)/(normal2)
            return 3*field[0]*RIGHT + 3*field[1]*UP
        
        north_pole = Rectangle(width=1,height=0.5,color=BLUE,fill_opacity=1).shift(LEFT*0.5)
        south_pole = Rectangle(width=1,height=0.5,color=RED,fill_opacity=1).shift(LEFT*-0.5)
        north_pole_tex = MathTex(r"N").move_to(north_pole)
        south_pole_tex = MathTex(r"S").move_to(south_pole)
        magnet = VGroup(north_pole,south_pole,north_pole_tex,south_pole_tex).move_to([0,0,0.1]).set_z_index(1)
        vector_field = ArrowVectorField(func=func1,max_color_scheme_value=0.3,min_color_scheme_value=0.01)
        stream = StreamLines(func1, stroke_width=2, max_anchors_per_line=600, virtual_time=90, n_repeats=4, max_color_scheme_value=1.1)

        p1 = Dot().scale(0.5)
        c1 = Circle(color=WHITE,radius=0.3)
        div_tex = MathTex(r"div\vec{B}=0")
        div_tex[0][3:5].set_color(YELLOW)
        s1 = SurroundingRectangle(div_tex,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)

        c1.add_updater(lambda mob: mob.move_to(p1))
        div_tex.add_updater(lambda mob: mob.next_to(c1,UP))
        s1.add_updater(lambda mob: mob.move_to(div_tex))

        self.play(Write(magnet))
        self.play(FadeIn(vector_field))
        self.wait()
        # self.add(stream)
        # stream.start_animation(flow_speed=4)
        self.play(FadeIn(p1,s1,c1,div_tex))
        self.play(p1.animate.move_to([0,1,0]),run_time=1)
        self.wait(2)
        self.play(p1.animate.move_to([2,0,0]),run_time=3)
        self.wait(2)
        self.play(p1.animate.move_to([0,-2,0]),run_time=3)
        self.wait(2)
        self.play(p1.animate.move_to([-2,0,0]),run_time=3)
        self.wait(2)

class Nabla2ndLaw(Scene):
    def construct(self):
        
        # Gauss's law for magnetism
        div_tex = MathTex(r"div",r"\vec{B}",r"=0")
        div_tex[1].set_color(YELLOW)
        div_formula = MathTex(r"\nabla \cdot",r"\vec{B}",r"=0").shift(UP*2)
        div_formula[1].set_color(YELLOW)


        self.play(Write(div_tex))
        self.wait(3)
        self.play(Write(div_formula))
        self.wait(3)
        self.play(div_tex.animate.to_corner(UL), div_formula.animate.to_corner(UR), run_time=2)

        # Nabla operator intro
        nabla_tex = MathTex(r"\nabla").scale(2).shift(UP)
        nabla_word = Tex("Nabla-Operator").next_to(nabla_tex, DOWN)

        self.wait()
        self.play(Write(nabla_tex))
        self.wait()
        self.play(Write(nabla_word))
        self.wait(5)

        # Show components
        nabla_components = MathTex(r"\nabla=\left [ \frac{\partial}{\partial x},\frac{\partial}{\partial y} \right ]").shift(DOWN*2)

        self.play(Write(nabla_components))
        self.wait(25)
        self.play(FadeOut(VGroup(nabla_tex,nabla_word,nabla_components)))

        # Magnetic field formula
        magnet_field1 = MathTex(r"\vec{B}",r"(x,y) = ",r"\frac{y-s}{x^2+(y-s)^2}",r"\hat{i}",r"- \frac{y+s}{x^2+(y+s)^2}",r"\hat{i}").shift(DOWN*-1.5).to_edge(LEFT)
        magnet_field2 = MathTex(r"+ \frac{-x}{x^2+(y-s)^2}",r"\hat{j}",r"+ \frac{x}{x^2+(y+s)^2}",r"\hat{j}").shift(DOWN*0.5).to_edge(LEFT)

        magnet_field1[0].set_color(YELLOW)
        self.wait(2)
        self.play(Write(magnet_field1), run_time=5)
        self.play(Write(magnet_field2), run_time=4)

        equation = MathTex(r"\nabla \cdot \vec{B} = \frac{\partial}{\partial x} B_{x} + \frac{\partial}{\partial y} B_{y}").shift(DOWN*3).to_edge(LEFT)

        self.wait(4)
        self.play(Write(equation))
        self.wait()

class GaussLawIntuition(Scene):
    def construct(self):

        law_tex = Tex("Gaußsches Gesetz")
        int_tex = Tex("Integrale Form:").shift(UP*0.5).to_edge(LEFT)
        dif_tex = Tex("Differentielle Form:").shift(UP*3).to_edge(LEFT)
        word_tex = Tex("Wortform:").shift(UP*-2).to_edge(LEFT)
        differential_form = MathTex(r" \nabla \cdot \vec{E} = \frac{\rho }{\varepsilon _{0}}").shift(UP*2).to_edge(LEFT)
        integral_form = MathTex(r"\oint_{A}\vec{E}\cdot d\vec{A}=\frac{q}{\varepsilon_{0}}").shift(UP*-0.5).to_edge(LEFT)
        word_form = Tex("Die elektrische Ladung ist Quelle des elektrischen Feldes.").shift(UP*-3).to_edge(LEFT)

        self.play(Write(law_tex))
        self.play(law_tex.animate.to_corner(UR))

        self.play(Write(dif_tex))
        self.wait()
        self.play(Write(differential_form))

        func1 = lambda pos: 3*(pos[0]/(pos[0]**2 + pos[1]**2 +0.0001)) * RIGHT + 3*(pos[1]/(pos[0]**2 + pos[1]**2 +0.0001)) * UP
        vector_field = ArrowVectorField(func1,x_range=[-3,3],y_range=[-1.5,2.5]).move_to([3.5,0.2,0])

        core = Circle(radius=0.4,color=RED,fill_opacity=1)
        corss1 = Rectangle(height=0.02,width=0.4,fill_opacity=1)
        corss2 = Rectangle(height=0.4,width=0.02,fill_opacity=1)
        proton = VGroup(core,corss1,corss2).scale(0.8).move_to([3.5,-0.2,0])

        b1 = SurroundingRectangle(vector_field,color=WHITE)

        self.wait(3)
        self.play(FadeIn(b1))
        self.play(FadeIn(proton))
        self.play(FadeIn(vector_field))
        self.wait(6)

        self.play(Write(int_tex))
        self.wait()
        self.play(Write(integral_form))
        self.wait(7)
        self.play(Write(word_tex))
        self.wait()
        self.play(Write(word_form))
        self.wait()

class GausDivergence(Scene):
    def construct(self):

        def vecField1(pos):
            e = 0.5
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = (x+2)/((x+2)**2 + y**2 + e) - (x-2)/((x-2)**2 + y**2 + e)
            field[1] = y/((x+2)**2 + y**2 + e) - y/((x-2)**2 + y**2 + e)
            return field[0]*RIGHT + field[1]*UP

        colors1 = [BLUE, YELLOW]
        vecField1Func1 = lambda pos: vecField1(pos=pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=2,min_color_scheme_value=0.01, colors=colors1).set_z_index(-1)
        stream = StreamLines(vecField1Func1, stroke_width=2, max_anchors_per_line=100, virtual_time=5, n_repeats=4, max_color_scheme_value=2, min_color_scheme_value=0.01, color=colors1).set_z_index(-1)
        
        p1 = Dot().scale(0.5)
        c1 = Circle(color=WHITE,radius=0.2)
        div_tex = MathTex(r"div\vec{E}=")
        div_tex[0][3:5].set_color(YELLOW)
        decnum = DecimalNumber(0)
        s1 = SurroundingRectangle(div_tex,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)
        s2 = SurroundingRectangle(decnum,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)

        c1.add_updater(lambda mob: mob.move_to(p1))
        div_tex.add_updater(lambda mob: mob.next_to(c1,UP))
        s1.add_updater(lambda mob: mob.move_to(div_tex))
        s2.add_updater(lambda mob: mob.move_to(decnum))
        decnum.add_updater(lambda mob: mob.next_to(c1,UP).shift(RIGHT*1.5))

        core = Circle(radius=0.4,color=RED,fill_opacity=1)
        corss1 = Rectangle(height=0.02,width=0.4,fill_opacity=1)
        corss2 = Rectangle(height=0.4,width=0.02,fill_opacity=1)
        proton = VGroup(core,corss1,corss2).shift(LEFT*2).scale(0.7)

        core1 = Circle(radius=0.4,color=PURE_GREEN,fill_color=PURE_GREEN,fill_opacity=1)
        corss3 = Rectangle(height=0.03,width=0.3,fill_opacity=1)
        electron = VGroup(core1,corss3).shift(RIGHT*2).scale(0.7)

        differential_form = MathTex(r" \nabla \cdot \vec{E} = \frac{\rho }{\varepsilon _{0}}").shift(UP*3)
        b1 = SurroundingRectangle(differential_form,color=BLACK,fill_color=BLACK,fill_opacity=0.9, stroke_opacity=0).move_to(differential_form)

        #fields
        self.wait()
        self.play(Write(vector_field1), Create(proton), Create(electron))
        self.wait(3)
        self.play(FadeIn(VGroup(b1,differential_form)))
        self.wait(6)
        self.add(stream)
        stream.start_animation(flow_speed=1.4)
        self.wait(5)

        self.play(FadeIn(p1,s1,s2,decnum,c1,div_tex))
        self.wait(2)
        self.play(p1.animate.move_to([2,0,0]), run_time=3)
        decnum.set_value(-1)
        self.wait(4)
        decnum.set_value(0)
        self.play(p1.animate.move_to([-2,0,0]), run_time=3)
        decnum.set_value(1)
        self.wait(5)

class GausChargeDensity(ThreeDScene):
    def construct(self):

        elambda = MathTex(r"[",r"\lambda",r"]",r"=\frac{C}{m}").shift(LEFT*5+ 2*DOWN)
        esigma = MathTex(r"[",r"\sigma ",r"]",r"=\frac{C}{m^{2}}").shift(LEFT*0+ 2*DOWN)
        erho = MathTex(r"[",r"\rho",r"]",r"=\frac{C}{m^{3}}").shift(LEFT*-5+ 2*DOWN)

        llam = Line(color=BLUE).shift(LEFT*5+ UP)
        csig = Circle(radius=1, color=BLUE, fill_opacity=1).shift(LEFT*0+ UP)
        srho = Sphere(radius=1).shift(LEFT*-5+ UP)

        self.play(Write(esigma[1]))
        self.wait()
        self.play(Write(esigma[0]), Write(esigma[2:]))
        self.wait(3)
        self.play(Create(csig))
        self.wait(3)

        self.play(Write(elambda[1]))
        self.wait(1)
        self.play(Write(elambda[0]), Write(elambda[2:]))
        self.wait(3)
        self.play(Create(llam))
        self.wait(3)

        self.play(Write(erho[1]))
        self.wait(1)
        self.play(Write(erho[0]), Write(erho[2:]))
        self.wait(3)
        self.play(Create(srho))
        self.wait(3)

#DesmosElectircField1

#DesmosElectircField2

class Gauss(ThreeDScene):
    def construct(self):

        #charge
        charge = Dot3D(color=RED).scale(2)

        self.move_camera(phi=60*DEGREES, zoom=3, run_time=0.01)
        self.begin_ambient_camera_rotation(rate=0.1)

        #vectors fielfd
        func1 = lambda pos: 3*(pos[0]/(pos[0]**2 + pos[1]**2 +0.0001)) * RIGHT + 3*(pos[1]/(pos[0]**2 + pos[1]**2 +0.0001)) * UP
        vector_field1 = ArrowVectorField(func1,x_range=[-8,8],y_range=[-8,8])
        vector_field2 = ArrowVectorField(func1,x_range=[-8,8],y_range=[-8,8]).rotate(PI/2,axis=RIGHT)

        arrows = VGroup(vector_field1,vector_field2)
        self.play(Create(charge),run_time=2)
        self.wait(2)
        self.play(FadeIn(arrows))

        #surface
        sphere = Sphere(resolution=(24,12)).rotate(PI/2, OUT)

        self.wait(5)
        self.play(arrows.animate.scale(2), run_time=2)
        self.wait(2)
        self.play(Create(sphere), run_time=4)

        #Law
        law_tex = MathTex(r"\oint_{A}\vec{E}\cdot d\vec{A} = \frac{q}{\varepsilon_{0}}").move_to([0,0,2])
        b1 = SurroundingRectangle(law_tex,color=BLACK,fill_color=BLACK,fill_opacity=0.7, stroke_opacity=0).move_to(law_tex)

        self.wait(3)
        self.add_fixed_orientation_mobjects(b1,law_tex)
        self.add_fixed_in_frame_mobjects(b1,law_tex)
        self.play(Write(law_tex),Write(b1))
        self.wait(8)

class VectorDotProductLabel(Scene):
    def construct(self):

        dotproduct2 = MathTex(r"\vec{v}",r"\cdot",r"\vec{w}").scale(1.7)
        dotproduct2[0].set_color(YELLOW)
        dotproduct2[2].set_color(BLUE)

        dotproduct = Tex("Skalarprodukt").shift(UP*2)
        ar1 = Arrow(dotproduct.get_bottom(), dotproduct2[1].get_top())


        #dot product intro
        self.wait()
        self.play(Write(dotproduct2))
        self.wait(3)

        self.play(Write(dotproduct), GrowArrow(ar1), run_time=2)
        self.play(Circumscribe(dotproduct2[1]))
        self.play(Indicate(dotproduct2[1]))

        self.wait()
        self.play(Unwrite(ar1))
        self.wait()


        #numberplane visual
        number_plane = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-5, 5, 1),
            x_length=4,
            y_length=4,
        ).move_to(LEFT*4.5).set_opacity(0.7)
        npV1 = number_plane.get_vector([3,2,0]).set_color(YELLOW)
        npW1 = number_plane.get_vector([4,1,0]).set_color(BLUE)

        self.play(Write(number_plane),run_time=2)
        self.wait()

        self.play(ReplacementTransform(dotproduct2[0].copy(),npV1),run_time=2)
        self.wait()

        self.play(ReplacementTransform(dotproduct2[2].copy(),npW1),run_time=2)

        #calculation
        vectorv = MathTex(r"\begin{bmatrix}3\\2\end{bmatrix}").shift(2*DOWN+LEFT)
        vectorv[0][0].set_color(YELLOW)
        vectorv[0][3].set_color(YELLOW)
        vectorv[0][1].set_color(RED)
        vectorv[0][2].set_color(GREEN)
        vectorw = MathTex(r"\begin{bmatrix}4\\1\end{bmatrix}").shift(2*DOWN+RIGHT)
        vectorw[0][0].set_color(BLUE)
        vectorw[0][3].set_color(BLUE)
        vectorw[0][1].set_color(RED)
        vectorw[0][2].set_color(GREEN)
        cdot = MathTex(r"\cdot").shift(2*DOWN)

        self.play(ReplacementTransform(dotproduct2[0].copy(),vectorv))
        self.wait()

        self.play(Write(cdot))
        self.wait()

        self.play(ReplacementTransform(dotproduct2[2].copy(),vectorw))

        #calc right side
        equals = MathTex(r"=").shift(2*DOWN+RIGHT*2)
        equation = MathTex(r"3\cdot 4",r"+",r"2\cdot1").shift(2*DOWN+RIGHT*4)
        equation[0].set_color(RED)
        equation[2].set_color(GREEN)
        equationCopy1 = VGroup(vectorv[0][1],vectorw[0][1]).copy()
        equationCopy2 = VGroup(vectorv[0][2],vectorw[0][2]).copy()

        self.wait()
        self.play(Write(equals))
        self.wait()
        self.play(ClockwiseTransform(equationCopy1,equation[0]),run_time=4)
        self.wait()
        self.play(FadeIn(equation[1]))
        self.wait()
        self.play(ClockwiseTransform(equationCopy2,equation[2]),run_time=4)

        #numberplane visual2
        npV2 = number_plane.get_vector([-4,4,0]).set_color(YELLOW)
        npW2 = number_plane.get_vector([-1,-3,0]).set_color(BLUE)

        self.wait(2)
        self.play(ReplacementTransform(npV1,npV2),run_time=2)
        self.wait()
        self.play(ReplacementTransform(npW1,npW2),run_time=2)
        self.wait()

        #calculation2
        vectorv2 = MathTex(r"\begin{bmatrix}-4\\4\end{bmatrix}").shift(2*DOWN+LEFT)
        vectorv2[0][0].set_color(YELLOW)
        vectorv2[0][4].set_color(YELLOW)
        vectorv2[0][1:3].set_color(RED)
        vectorv2[0][3].set_color(GREEN)
        vectorw2 = MathTex(r"\begin{bmatrix}-1\\-3\end{bmatrix}").shift(2*DOWN+RIGHT)
        vectorw2[0][0].set_color(BLUE)
        vectorw2[0][5].set_color(BLUE)
        vectorw2[0][1:3].set_color(RED)
        vectorw2[0][3:5].set_color(GREEN)

        self.play(Unwrite(VGroup(vectorv,vectorw)))
        self.play(Unwrite(equationCopy1),Unwrite(equationCopy2), Unwrite(equation))
        self.play(ReplacementTransform(dotproduct2[0].copy(),vectorv2))
        self.wait()
        self.play(ReplacementTransform(dotproduct2[2].copy(),vectorw2))
        self.wait()

        #calc right side
        equationCopy3 = VGroup(vectorv2[0][1:3],vectorw2[0][1:3]).copy()
        equationCopy4 = VGroup(vectorv2[0][3],vectorw2[0][3]).copy()
        equation2 = MathTex(r"-4\cdot -1",r"+",r"4\cdot -3").shift(2*DOWN+RIGHT*4)
        equation2[0].set_color(RED)
        equation2[2].set_color(GREEN)

        self.wait()
        self.play(ClockwiseTransform(equationCopy3,equation2[0]), run_time=3)
        self.wait()
        self.play(FadeIn(equation2[1]))
        self.wait()
        self.play(ClockwiseTransform(equationCopy4,equation2[2]), run_time=3)
        self.wait()

class VectorDotProduct(Scene):
    def construct(self): 

        nump = NumberPlane().set_opacity(0.4)
        v_vec = nump.get_vector([3,1,0],color=YELLOW)
        w_vec = nump.get_vector([1,3,0],color=RED)
        v_vectex = MathTex(r"\vec{v}", color=YELLOW)
        w_vectex = MathTex(r"\vec{w}", color=RED)
        v_vectex.add_updater(lambda mob: mob.move_to(v_vec).shift(RIGHT*0.5 + DOWN*0.5))
        w_vectex.add_updater(lambda mob: mob.move_to(w_vec).shift(LEFT*0.5 + UP*0.5))

        dotproduct = Tex("Skalarprodukt").to_corner(UL) 
        dotproduct2 = MathTex(r"\vec{v}",r"\cdot",r"\vec{w}").next_to(dotproduct,RIGHT)
        dotproduct2[0].set_color(YELLOW)
        dotproduct2[2].set_color(RED)
        line = Line(start=[-12,-4,0],end=[12,4,0]).set_z_index(-1)

        #init
        self.wait()
        self.play(FadeIn(nump))
        self.wait()
        self.play(GrowArrow(v_vec), FadeIn(v_vectex),run_time=1.5)
        self.play(GrowArrow(w_vec), FadeIn(w_vectex),run_time=1.5)
        self.wait()
        self.play(Write(VGroup(dotproduct,dotproduct2)))


        #geometric projection
        conetctLine = Line(end=[1.8,0.6,0], start=[2*w_vec.get_x(),2*w_vec.get_y(),0])
        projectVector = Vector([0,0,0],color=RED)
        projectVector.add_updater(lambda mob: mob.become(Vector(
            [3*(3*2*w_vec.get_x()+2*w_vec.get_y())/np.sqrt(100),
             1*(3*2*w_vec.get_x()+2*w_vec.get_y())/np.sqrt(100),0],
             color = GREEN
            )))
        rightan = Angle(conetctLine,line, dot=True, quadrant=(-1,1), other_angle=True)

        self.wait(3)
        self.play(GrowFromCenter(line), run_time=3)
        self.play(Indicate(VGroup(v_vec,v_vectex)))
        self.wait()
        self.play(Write(conetctLine), run_time=3)
        self.wait(2)
        self.play(ReplacementTransform(w_vec.copy(),projectVector), run_time=5)
        self.wait()
        self.play(GrowFromPoint(rightan, projectVector.get_end()))
        self.wait(3)

        #equation
        eqation1 = MathTex(r"\vec{v}",r"\cdot",r"\vec{w}", r">",r"0").shift(RIGHT*2+DOWN*1.5)
        eqation1[0].set_color(YELLOW)
        eqation1[2].set_color(RED)

        self.play(Write(eqation1))

        #next positions example
        eqation2 = MathTex(r"\vec{v}",r"\cdot",r"\vec{w}", r"<",r"0").shift(RIGHT*2+DOWN*1.5)
        eqation2[0].set_color(YELLOW)
        eqation2[2].set_color(RED)
        eqation3 = MathTex(r"\vec{v}",r"\cdot",r"\vec{w}", r"=",r"0").shift(RIGHT*2+DOWN*1.5)
        eqation3[0].set_color(YELLOW)
        eqation3[2].set_color(RED)

        self.play(Unwrite(rightan))
        self.play(Unwrite(conetctLine))
        self.wait(3)

        self.play(w_vec.animate.rotate_about_origin(PI), run_time=3)
        self.play(Indicate(eqation1))
        self.play(TransformMatchingShapes(eqation1,eqation2))
        self.wait(6)

        self.play(w_vec.animate.rotate_about_origin(PI+0.6435), run_time=3)
        self.play(Indicate(eqation2))
        self.play(TransformMatchingShapes(eqation2,eqation3))
        self.wait(6)

        #rotation and calc
        dotp = ValueTracker()
        dotp.add_updater(lambda mob: mob.set_value(4*(projectVector.get_x()*v_vec.get_x() + projectVector.get_y()*v_vec.get_y())))
        number = DecimalNumber(0,num_decimal_places=2).next_to(eqation3[3], RIGHT, buff=0.4)
        number.add_updater(lambda mob: mob.set_value(dotp.get_value()))

        self.add(dotp)
        self.play(FadeOut(eqation3[4]))
        self.play(FadeIn(number))
        self.wait()

        self.play(Rotate(w_vec,2*PI,about_point=ORIGIN), rate_func=linear, run_time=7)
        self.play(Rotate(w_vec,-2*PI,about_point=ORIGIN), rate_func=linear, run_time=20)
        self.wait()

class Flux(Scene):
    def construct(self):

        positive_plate = Rectangle(height=4,width=0.5,color=RED,fill_opacity=1).shift(LEFT*6)
        positive_plate2 = Polygon(positive_plate.get_corner(UR),positive_plate.get_corner(DR),positive_plate.get_corner(DR)+[0.2,0.4,0],positive_plate.get_corner(UR)+[0.2,-0.4,0],fill_opacity=1,color=ManimColor.from_rgb((160,30,30, 1)))
        negativ_plate = Rectangle(height=4,width=0.5,color=GREEN,fill_opacity=1).shift(RIGHT*6)
        negativ_plate2 = Polygon(negativ_plate.get_corner(UL),negativ_plate.get_corner(DL),negativ_plate.get_corner(DL)+[-0.2,0.4,0],negativ_plate.get_corner(UL)+[-0.2,-0.4,0],fill_opacity=1,color=ManimColor.from_rgb((16,140,16, 1)))

        field_line1 = Arrow([-6,2,0],[6,2,0])
        field_line2 = Arrow([-6,1,0],[6,1,0])
        field_line3 = Arrow([-6,0,0],[6,0,0])
        field_line4 = Arrow([-6,-1,0],[6,-1,0])
        field_line5 = Arrow([-6,-2,0],[6,-2,0])
        fieldLines = VGroup(field_line1,field_line2,field_line3,field_line4,field_line5)

        #condensator fieldlines
        self.wait()
        self.play(Write(positive_plate),Write(positive_plate2))
        self.wait()
        self.play(Write(negativ_plate), Write(negativ_plate2))
        self.wait(4)
        self.play(AnimationGroup(GrowArrow(fieldLines[0]),GrowArrow(fieldLines[1]),GrowArrow(fieldLines[2]),GrowArrow(fieldLines[3]),GrowArrow(fieldLines[4]), lag_ratio=0.7), run_time=6)

        #introduce surface
        plane_surface = Rectangle(height=4,width=0.25,fill_opacity=1,color=BLUE).set_z_index(1)
        plane_surface2 = Polygon(plane_surface.get_corner(UR),plane_surface.get_corner(DR),plane_surface.get_corner(DR)+[0.2,0.4,0],plane_surface.get_corner(UR)+[0.2,-0.4,0],fill_opacity=1,color=DARK_BLUE).set_z_index(-1)

        self.wait(2)
        self.play(VGroup(negativ_plate,negativ_plate2).animate.shift(RIGHT*2), run_time=3)
        self.wait(2)
        self.play(Write(plane_surface),Write(plane_surface2), run_time=2)

        #show flux
        flux_tex = Tex("Fluss").shift(UP*3).scale(1.5)
        func1 = lambda pos: RIGHT
        stream = StreamLines(func1, stroke_width=4, max_anchors_per_line=25, virtual_time=50, n_repeats=15,
                             x_range=[-5.7,5,7],y_range=[-2,2])

        self.wait(2)
        self.play(Write(flux_tex))
        self.wait(3)
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=5)
        self.wait(10)

        #equation
        forumla = MathTex(r"\phi = E \cdot A").shift(UP*3)
        forumla[0][2].set_color(GREEN)
        forumla[0][4].set_color(BLUE)

        self.play(flux_tex.animate.to_edge(LEFT))
        self.play(Write(forumla))
        self.play(stream.animate.set_opacity(0), fieldLines.animate.set_opacity(0.2))
        stream.end_animation()
        self.remove(stream)

        #vectors e,n
        normal_vector = Vector([2,0],color=RED)
        normal_vector_tex = MathTex(r"\hat{n}").set_color(RED).next_to(normal_vector,DOWN).set_z_index(2)
        e_vector = Vector([2,0],color=GREEN)

        vecE = MathTex(r"\vec{E}").next_to(positive_plate,DR)
        area = MathTex(r"A").next_to(plane_surface,DOWN).set_color(BLUE)

        self.wait(7)
        self.play(ReplacementTransform(forumla[0][2].copy(),vecE),run_time=2)
        self.wait(4)
        self.play(ReplacementTransform(forumla[0][4].copy(),area),run_time=1.5)
        self.wait(4)
        self.play(GrowArrow(normal_vector), run_time=2)
        self.wait(6)
        self.play(Write(normal_vector_tex))

        self.wait(2)
        self.play(vecE.animate.next_to(e_vector,UP).set_color(GREEN))
        self.wait(2)
        self.play(GrowArrow(e_vector))
        self.wait(3)

        #new formula
        forumla2 = MathTex(r"\phi = \vec{E} \cdot \hat{n} \cdot A").shift(UP*3)
        forumla2[0][2:4].set_color(GREEN)
        forumla2[0][5:7].set_color(RED)
        forumla2[0][8].set_color(BLUE)
        normal_vector_tex.add_updater(lambda mob: mob.next_to(normal_vector,DOWN))

        self.play(normal_vector.animate.rotate_about_origin(PI/4), VGroup(plane_surface,plane_surface2).animate.rotate_about_origin(PI/4), run_time=3)
        self.wait(7)
        self.play(ReplacementTransform(forumla,forumla2))
        self.wait(6)

        #rotate change
        forumla3 = MathTex(r"\phi = \vec{E} \cdot \hat{n} \cdot A=").shift(UP*3).align_to(forumla2,LEFT)
        forumla3[0][2:4].set_color(GREEN)
        forumla3[0][5:7].set_color(RED)
        forumla3[0][8].set_color(BLUE)

        angle = ValueTracker(PI/4)
        value = DecimalNumber(0.707,num_decimal_places=2).next_to(forumla3,RIGHT)
        value.add_updater(lambda mob: mob.set_value(np.cos(angle.get_value())))

        self.play(TransformMatchingShapes(forumla2,forumla3))
        self.wait(3)
        self.play(Write(value))
        self.wait(5)
        self.play(VGroup(plane_surface,plane_surface2,normal_vector).animate.rotate_about_origin(PI/4),angle.animate.set_value(PI/2), run_time=3)
        self.wait(4)
        self.play(VGroup(plane_surface,plane_surface2,normal_vector).animate.rotate_about_origin(PI/2),angle.animate.set_value(PI), run_time=3)
        self.wait(4)
        self.play(VGroup(plane_surface,plane_surface2,normal_vector).animate.rotate_about_origin(PI/2),angle.animate.set_value(3*PI/2), run_time=3)
        self.wait(4)
        self.play(VGroup(plane_surface,plane_surface2,normal_vector).animate.rotate_about_origin(3*PI/8),angle.animate.set_value(15*PI/8), run_time=3)
        self.wait(4)

        #surface element
        surface_element = MathTex(r"\vec{A}=\hat{n}\cdot A").shift(UP*3).next_to(plane_surface,LEFT)
        forumla4 = MathTex(r"\phi = \vec{E} \cdot \vec{A}").shift(UP*3).align_to(forumla2,LEFT)
        forumla4[0][2:4].set_color(GREEN)
        forumla4[0][5:7].set_color(RED)

        self.wait()
        self.play(Write(surface_element))
        self.wait(5)
        self.play(ReplacementTransform(forumla3,forumla4), FadeOut(value), run_time=2)
        self.wait()

class IngegralIntro(Scene):
    def construct(self):   

        axes = Axes(x_range=[0,5,1],y_range=[0,4,1], x_length=5, y_length=4,axis_config={"include_numbers": True}).shift(2*LEFT)
        graph = axes.plot(lambda x: 2).set_color(GREEN)
        vtex = MathTex(r"v").align_to(axes,UL).shift(UP*0.5+RIGHT*0.3)
        vtex2 = Tex("in").next_to(vtex,RIGHT)
        vtex3= MathTex(r"\frac{m}{s}").scale(1).next_to(vtex2,RIGHT)
        ttex = MathTex(r"t").align_to(axes,DR).shift(RIGHT*0.5 +UP*0.3)
        ttex2 = Tex("in").next_to(ttex,RIGHT)
        ttex3 = MathTex(r"s").next_to(ttex2,RIGHT)
        labels = VGroup(vtex,vtex2,vtex3,ttex,ttex2,ttex3)

        rect = axes.get_riemann_rectangles(graph=graph,x_range=[0,5],dx=5).set_opacity(0.5).set_color(BLUE)
        bracedx = Brace(rect,DOWN).shift(DOWN*0.4)
        bracedf = Brace(rect,LEFT).shift(LEFT*0.4)
        dftex = MathTex(r"2\frac{m}{s}").next_to(bracedf,LEFT).set_color(GREEN)
        dxtex = MathTex(r"5s").next_to(bracedx,DOWN).set_color(YELLOW)

        equation = MathTex(r"s=2\frac{m}{s}\cdot5s=10m").to_corner(UR)

        #start
        self.play(Write(axes),Write(graph))
        self.wait()
        self.play(Write(labels), run_time=3)
        self.wait()

        self.play(Indicate(graph))
        self.wait()

        sq = MathTex(r"s=?").to_edge(UP)
        svt = MathTex(r"s=v\cdot t").to_edge(UP)
        svt[0][2].set_color(GREEN)
        svt[0][4].set_color(YELLOW)

        #frage
        self.play(Write(sq))
        self.wait(2)
        self.play(ReplacementTransform(sq,svt))
        self.wait(3)

        #Lösung
        self.play(Write(dftex))
        self.wait()
        self.play(Write(dxtex))
        self.wait()
        self.play(Write(equation), run_time=2)
        self.wait()
        self.play(Unwrite(svt))

        #observation
        self.play(FadeIn(rect))
        self.wait(2)
        self.play(Write(bracedf))
        self.play(Write(bracedx))
        self.wait(2)
        #area
        area = MathTex(r"[",r"A",r"]",r"=\frac{m}{s}\cdot s=m").move_to(rect)
        area[0][2:5].set_color(GREEN)
        area[0][6:7].set_color(YELLOW)

        self.play(Write(area[1]))
        self.wait(3)
        self.play(Write(area[0]),Write(area[2:]))

        aiss = MathTex(r"s=A").next_to(equation, DOWN).align_to(equation,LEFT)
        self.wait(5)
        self.play(Write(aiss))
        self.play(Indicate(aiss))
        self.wait(2)

        #bezug integral
        integral = MathTex(r"s=\int_{}^{}2\frac{m}{s}\cdot 5s=10m").next_to(aiss,DOWN).to_edge(RIGHT)
        self.play(Write(integral))
        self.wait()

class IngegralTriangle(Scene):
    def construct(self):  

        axes = Axes(x_range=[0,6,1],y_range=[0,6,1], x_length=6, y_length=6,axis_config={"include_numbers": True}).shift(2*LEFT)
        graph1 = axes.plot(lambda x: 3).set_color(GREEN)
        graph2 = axes.plot(lambda x: x).set_color(GREEN)
        graph3 = axes.plot(lambda x: -0.5*x*x+3*x).set_color(GREEN)
        vtex = MathTex(r"v").align_to(axes,UL).shift(UP*0.4)
        ttex = MathTex(r"t").align_to(axes,DR).shift(RIGHT*0.5)

        rect1 = axes.get_riemann_rectangles(graph=graph1,x_range=[0,6],dx=0.01).set_opacity(0.5).set_color(BLUE)
        rect2 = axes.get_riemann_rectangles(graph=graph2,x_range=[0,6],dx=0.01).set_opacity(0.5).set_color(BLUE)
        rect3 = axes.get_riemann_rectangles(graph=graph3,x_range=[0,6],dx=0.01).set_opacity(0.5).set_color(BLUE)

        area = MathTex(r"A",color=YELLOW).move_to(rect1).scale(1.5)
        a1 = MathTex(r"A=6\cdot 3").shift(RIGHT*4.5).scale(1.5)
        a2 = MathTex(r"A=\frac{1}{2}\cdot 6 \cdot 6").shift(RIGHT*4.5).scale(1.5)
        a3 = MathTex(r"A=?").shift(RIGHT*4.5).scale(1.5)
        a1[0][0].set_color(YELLOW)
        a2[0][0].set_color(YELLOW)
        a3[0][0].set_color(YELLOW)
        
        #setup
        self.wait()
        self.play(Write(axes),Write(graph1),Write(vtex),Write(ttex))
        self.wait()
        self.play(Write(rect1), run_time=1)

        #area
        self.play(Write(area))
        self.play(Write(a1))
        self.wait()

        #area2
        self.wait(2) 
        self.play(ReplacementTransform(graph1,graph2),ReplacementTransform(rect1,rect2), run_time=2)
        self.play(ReplacementTransform(a1,a2), run_time=1)
        self.wait(4)

        #area3 no solution
        self.play(ReplacementTransform(graph2,graph3),ReplacementTransform(rect2,rect3), run_time=2)
        self.play(ReplacementTransform(a2,a3))
        self.wait()

class IngegralFineRectangles(Scene):
    def construct(self):      

        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=12,
            y_length=6,
        ).shift(UP*0.7)
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        def f(x):
            return 0.25*x**3 - 1.3*x**2 + 1.4*x + 1.1

        graph = axes.plot(f, x_range=[0, 5], color=BLUE)

        d = ValueTracker(1)
        opacity = ValueTracker(0)

        finer_rects = axes.get_riemann_rectangles(graph)
        finer_rects.add_updater(lambda mob: mob.become( axes.get_riemann_rectangles(
            graph,
            x_range=[0, 5],
            dx=d.get_value(),
            input_sample_type="left",
            fill_opacity=opacity.get_value(),
        )))

        area = MathTex(r"A=?").shift(UP*3).scale(1.5)
        arrow1 = Arrow([0,2,0],[-1.4,0.3,0])
        arrow2 = Arrow([0,2,0],[0.6,-1.3,0])
        arrow3 = Arrow([0,2,0],[3.3,-1.3,0])
        arrows = VGroup(arrow1,arrow3,arrow2).set_color(YELLOW)

        #build
        self.wait()
        self.play(Create(graph))
        self.play(Write(axes), Write(labels))
        self.play(Write(area))
        self.wait(2)
        self.play(FadeIn(finer_rects))
        self.wait(5)
        self.play(opacity.animate.set_value(0.7))

        #show overlap
        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        self.play(GrowArrow(arrow3))
        self.wait(5)

        #show smaller rectangles
        self.play(Unwrite(arrows))
        self.wait()
        self.play(d.animate.set_value(0.5), run_time=5)
        self.play(d.animate.set_value(0.25), run_time=5)
        self.play(d.animate.set_value(0.1), run_time=5)
        self.play(d.animate.set_value(0.01), opacity.animate.set_value(1), run_time=5)
        self.wait()

class IngegralExplanation(Scene):
    def construct(self): 

        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=12,
            y_length=6,
        ).shift(UP*0.7)
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        def f(x):
            return 0.25*x**3 - 1.3*x**2 + 1.4*x + 1.1

        graph = axes.plot(f, x_range=[0, 5], color=BLUE).set_z_index(-2)

        rect = axes.get_riemann_rectangles(graph,fill_opacity=0.5,x_range=[1,5],dx=1).set_z_index(-2)
        dx_tex = MathTex(r"dx").set_color(YELLOW)
        fx_tex = MathTex(r"f(x)").set_color(GREEN)
        b1 = SurroundingRectangle(fx_tex,corner_radius=0.3,fill_opacity=0.7,color=BLACK,stroke_opacity=0).set_z_index(-1)
        b1.add_updater(lambda mob: mob.move_to(fx_tex))

        A_tex = MathTex(r"dA").move_to(rect[0]).set_color(WHITE)
        A_calc = MathTex(r"dA=",r"f(x)",r"\cdot",r"dx").shift(RIGHT*0 + UP*3).set_color(WHITE)
        A_calc[1].set_color(GREEN)
        A_calc[3].set_color(YELLOW)

        b2 = SurroundingRectangle(A_tex,corner_radius=0.2,fill_opacity=0.7,color=BLACK,stroke_opacity=0).set_z_index(-1)
        b2.add_updater(lambda mob: mob.move_to(A_tex))

        A_word1 = MathTex(r"A=").shift(RIGHT*0 + UP*3).set_color(WHITE)
        A_word2 = Tex("Summe von").next_to(A_word1,RIGHT).set_color(WHITE)
        A_word3 = MathTex(r"dA").next_to(A_word2,RIGHT).set_color(WHITE)
        awords = VGroup(A_word1,A_word2,A_word3).move_to(A_calc)
        A_word4 = MathTex(r'"\int umme"').next_to(awords,DOWN).set_color(WHITE)
        A_word4[0][1].set_color(YELLOW)

        A_calc2 = MathTex(r" A=\int_{}^{}dA").shift(RIGHT*0 + UP*1.5).set_color(WHITE)
        A_calc2[0][2].set_color(YELLOW)
        A_calc3 = MathTex(r" A=\int_{}^{}f(x)dx").shift(RIGHT*1 + UP*0.1).set_color(WHITE)
        A_calc3[0][2].set_color(YELLOW)
        A_calc4 = MathTex(r" A=\int_{1}^{5}f(x)dx").shift(RIGHT*0 + UP*2).set_color(WHITE)
        A_calc4[0][3:5].set_color(YELLOW)

        brace_dx = Brace(rect[0],DOWN)
        brace_fx = Brace(rect[0],LEFT)

        dx_tex.add_updater(lambda mob: mob.next_to(brace_dx,DOWN))
        fx_tex.add_updater(lambda mob: mob.next_to(brace_fx,LEFT))

        #build
        self.wait()
        self.play(Create(graph))
        self.play(Write(axes), Write(labels))
        self.play(Write(rect))

        #df dx
        self.wait()
        self.play(Write(brace_dx))
        self.play(Write(dx_tex))
        self.wait(7)
        self.play(Write(brace_fx))
        self.play(Write(VGroup(fx_tex,b1)))
        self.wait(4)

        #area def
        self.play(Write(VGroup(A_tex,b2)))
        self.wait(5)
        self.play(ReplacementTransform(A_tex.copy(),A_calc[0]))
        self.play(ReplacementTransform(fx_tex.copy(),A_calc[1]), Write(A_calc[2]))
        self.play(ReplacementTransform(dx_tex.copy(),A_calc[3]))

        #hop over rectangles
        self.wait(4)
        self.play(brace_dx.animate.become(Brace(rect[1],DOWN)), brace_fx.animate.become(Brace(rect[1],LEFT)), A_tex.animate.move_to(rect[1]),run_time=3)
        self.play(brace_dx.animate.become(Brace(rect[2],DOWN)), brace_fx.animate.become(Brace(rect[2],LEFT)), A_tex.animate.move_to(rect[2]),run_time=3)
        self.play(brace_dx.animate.become(Brace(rect[3],DOWN)), brace_fx.animate.become(Brace(rect[3],LEFT)), A_tex.animate.move_to(rect[3]),run_time=3)

        #meaning of A
        self.play(Unwrite(VGroup(brace_dx,brace_fx,fx_tex,dx_tex,b1,b2,A_tex)))
        self.wait()
        self.play(ReplacementTransform(A_calc, awords), run_time=2)

        dA1 = MathTex(r"dA").move_to(rect[0])
        dA2 = MathTex(r"dA").move_to(rect[1])
        dA3 = MathTex(r"dA").move_to(rect[2])
        dA4 = MathTex(r"dA").move_to(rect[3])
        self.play(Write(VGroup(dA1,dA2,dA3,dA4)))
        self.wait()
        self.play(AnimationGroup(dA1.animate.move_to(awords[0]).set_opacity(0),
                                 dA2.animate.move_to(awords[0]).set_opacity(0),
                                 dA3.animate.move_to(awords[0]).set_opacity(0),
                                 dA4.animate.move_to(awords[0]).set_opacity(0),lag_ratio=0.8), run_time=4)

        #int explain
        self.play(awords[1][0][0:5].animate.set_color(YELLOW))
        self.wait(2)
        self.play(Write(A_word4))
        self.wait(5)
        self.play(ReplacementTransform(A_word4, A_calc2))
        self.wait(4)
        self.play(ReplacementTransform(A_calc2.copy(), A_calc3))
        self.wait(4)


        #add domain
        x0 = MathTex(r"x=1").shift(LEFT*3.5+DOWN*3)
        x1 = MathTex(r"x=5").shift(LEFT*-5.7+DOWN*3)
        x0[0][2].set_color(YELLOW)
        x1[0][2].set_color(YELLOW)

        self.play(Write(x0))
        self.play(Write(x1))
        self.wait(2)

        self.play(Unwrite(VGroup(A_calc2,awords)))
        self.play(A_calc3.animate.move_to([0,2,0]))
        self.wait(2)

        self.play(ReplacementTransform(A_calc3,A_calc4), x0.copy().animate.move_to(A_calc4).set_opacity(0),
                   x1.copy().animate.move_to(A_calc4).set_opacity(0), run_time=3)
        self.wait()

class FluxIntegral(ThreeDScene):
    def construct(self):
        
        #known setup
        surface = Rectangle(width=4,height=4,color=BLUE,fill_opacity=1)
        area = MathTex(r"A").set_color(BLUE).shift(LEFT*3)
        formula = MathTex(r"\phi=",r"\vec{E}",r"\cdot",r"\vec{A}").shift(UP*3)
        formula[1].set_color(GREEN)
        formula[3].set_color(RED)

        self.wait()
        self.play(DrawBorderThenFill(surface))
        self.wait()
        self.play(Write(area))
        self.wait()
        self.play(Write(formula))
        self.wait(3)


        #dphi/dA
        formula2 = MathTex(r"d\phi=",r"\vec{E}",r"\cdot",r"d\vec{A}").shift(UP*3)        
        formula2[1].set_color(GREEN)
        formula2[3].set_color(RED)
        
        surface_element = MathTex(r"d\vec{A}",r"=\hat{n}\cdot",r"dA").next_to(surface,RIGHT)
        surface_elementOld = MathTex(r"\vec{A}",r"=\hat{n}\cdot",r"A").next_to(surface_element,UP).align_to(surface_element,LEFT)
        surface_element[0].set_color(RED)
        surface_element[2].set_color(YELLOW)
        surface_elementOld[0].set_color(RED)
        surface_elementOld[2].set_color(YELLOW)

        rect = Rectangle(width=1,height=1,color=YELLOW)
        da = MathTex(r"dA").set_color(YELLOW).next_to(rect,RIGHT)

        self.play(DrawBorderThenFill(rect))
        self.play(GrowFromEdge(da,LEFT))
        self.wait(3)
        self.play(VGroup(rect,da).animate.scale(0.01), run_time=3)
        self.wait(2)
        self.play(VGroup(rect,da).animate.scale(100), run_time=3)

        self.wait(2)
        self.play(Write(surface_elementOld))
        self.wait(3)
        self.play(ReplacementTransform(surface_elementOld.copy(),surface_element))
        self.wait(7)

        self.play(Circumscribe(formula))
        self.play(ReplacementTransform(formula,formula2))
        self.wait(2)


        #integral form
        formula3 = MathTex(r"\int_{A}^{} d\phi= \int_{A}^{}",r"\vec{E}",r"\cdot",r"d\vec{A}").shift(UP*3)        
        formula3[1].set_color(GREEN)
        formula3[3].set_color(RED)

        n = 20
        dx = surface.width / n
        dy = surface.height / n
        dA_tiles = VGroup()

        for i in range(n):
            for j in range(n):
                tile = Rectangle(width=dx, height=dy,color=YELLOW)
                tile.move_to(surface.get_corner(DL) + RIGHT * (i + 0.5) * dx + UP * (j + 0.5) * dy)
                dA_tiles.add(tile)

        self.wait()
        self.play(Circumscribe(formula2[0][0:2]))
        self.wait()
        self.play(ReplacementTransform(formula2,formula3))
        self.wait(10)

        self.play(FadeOut(rect))
        self.play(da.animate.next_to(surface,DOWN))
        self.play(LaggedStart( *[FadeIn(tile, scale=0.5) for tile in dA_tiles], lag_ratio=0.02))

        #integral cancel
        self.wait(1)
        self.play(Circumscribe(formula3[0][0:4]))
        self.wait()
        self.play(FadeOut(formula3[0][0:3]))

        #realise complexity
        self.play(dA_tiles.animate.set_opacity(0),FadeOut(da))
        self.wait(5)
        self.move_camera(phi=60*DEGREES,theta=-80*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.4, about= "theta")
        self.wait(5)

        #to sphere
        sphere = Sphere(radius=2,color=BLUE)

        self.play(FadeTransform(surface,sphere), run_time=3)
        self.wait(5)
        self.move_camera(phi=0,theta=-PI/2 +2*PI, run_time=3)
        self.stop_ambient_camera_rotation()

        closed_int = MathTex(r"\oint_{A}^{}").set_color(YELLOW).move_to(formula3[0][5:7])
        self.wait(3)
        self.play(ReplacementTransform(formula3[0][5:7], closed_int))
        self.wait(3)

        self.move_camera(phi=60*DEGREES,theta=-80*DEGREES + 2*PI)
        self.begin_ambient_camera_rotation(rate=0.4, about= "theta")

        #show matrix
        matrix1 = [
            [-1,0,0],
            [0,-1,0],
            [0,0,0.4],
        ]
        matrix2 = [
            [1,0.4,-0.7],
            [0,-1.1,0.6],
            [0.1,-0.4,0.4],
        ]
        matrix3 = [
            [1.4,-0.4,-1.7],
            [-0.01,0,0.3],
            [0.14,-1.4,0.9],
        ]
        self.wait(3)
        self.play(sphere.animate.apply_matrix(matrix=matrix1), run_time=5)
        self.play(sphere.animate.apply_matrix(matrix=matrix2), run_time=5)
        self.play(sphere.animate.apply_matrix(matrix=matrix3), run_time=5)
        self.wait(3)

class GaussLawDerivation(ThreeDScene):
    def construct(self):

        #setup
        formula = MathTex(r"\oint_{A}",r"\vec{E}",r"\cdot",r"d\vec{A}")

        core = Circle(radius=0.4,color=RED,fill_opacity=1)
        corss1 = Rectangle(height=0.02,width=0.4,fill_opacity=1)
        corss2 = Rectangle(height=0.4,width=0.02,fill_opacity=1)
        proton = VGroup(core,corss1,corss2)
        circle = Circle(radius=2.5,color=BLUE)

        self.wait()
        self.play(Write(formula))
        self.wait()
        self.play(formula.animate.to_corner(UL))
        self.wait()
        self.play(Create(proton))
        self.wait()
        self.play(Write(circle))
        self.wait()

        #sphere
        sphere = Sphere().rotate(PI/4,axis=RIGHT).scale(2.5)
        self.wait()
        self.play(Create(sphere))
        self.play(Rotate(sphere, 3*PI, axis=UP), run_time=5)
        self.play(sphere.animate.shift(-5.5*RIGHT+2*DOWN).scale(1/2.5), run_time=1.5)
        self.wait()

        #r is n 
        da = MathTex(r"d",r"\vec{A}",r"=",r"\hat{n}",r"\cdot",r"dA").shift(UP*3)
        da[3].set_color(RED)
        n_vec = Vector([1,0]).next_to(circle,RIGHT,buff=0).set_color(RED)
        nhat = MathTex(r"\hat{n}").next_to(n_vec,UP).set_color(RED)

        r_vec = Vector([2.1,0]).next_to(core,RIGHT,buff=0).set_color(YELLOW)
        rhat = MathTex(r"\vec{r}").next_to(r_vec,UP).set_color(YELLOW)       
        risn = MathTex(r"\hat{r}",r"=",r"\hat{n}").move_to([4,2,0])       
        risn[0].set_color(YELLOW)
        risn[2].set_color(RED)

        self.play(ReplacementTransform(formula[3].copy(),da),run_time=3)
        self.wait(2)
        self.play(ReplacementTransform(da[3].copy(),nhat),GrowArrow(n_vec),run_time=3)
        self.wait(2)
        self.play(Write(rhat),GrowArrow(r_vec))
        self.wait(2)

        self.play(Write(risn))
        self.wait(2)
        self.play(Rotate(VGroup(nhat,rhat,n_vec,r_vec),2*PI,about_point=ORIGIN), run_time=7)
        self.play(Rotate(VGroup(nhat,rhat,n_vec,r_vec),-2*PI,about_point=ORIGIN), run_time=7)

        #reinsert
        da2 = MathTex(r"d\vec{A}=",r"\hat{r}",r"\cdot dA").shift(UP*3)
        da2[1].set_color(YELLOW)

        self.wait()
        self.play(FadeOut(da),ReplacementTransform(risn,da2),run_time=2)
        self.wait()
        self.play(FadeOut(VGroup(circle,rhat,r_vec,nhat,n_vec)))
        self.wait()

        self.play(FadeOut(da2[0]),FadeOut(formula[3]))
        self.wait()
        self.play(formula[0:3].animate.next_to(da2[1],LEFT).shift(DOWN*0.07))
        self.wait()

        #constants
        e_con = MathTex(r"E").shift(UP*1)
        formula2 = MathTex(r"\oint_{A}",r"dA").shift(UP*3)

        self.wait()
        self.play(FadeOut(proton))
        self.wait()
        self.play(VGroup(formula[1:3],da2[1]).animate.shift(DOWN*2))
        self.wait(14)

        self.play(ReplacementTransform(VGroup(formula[1:3],da2[1]), e_con))
        self.wait()

        self.play(e_con.animate.shift(UP*2))
        self.wait(1)
        self.play(e_con.animate.shift(LEFT*1), FadeOut(VGroup(formula[0],da2[2])), FadeIn(formula2))
        self.wait(6)

        #back to sphere
        self.wait()
        self.play(sphere.animate.move_to([0,-0.7,0]))
        self.wait()
        self.play(sphere.animate.scale(2.5))
        self.wait(3)

        #area
        area = MathTex(r"A=",r"4\pi r^{2}").move_to([5,0,0])
        area2 = MathTex(r"4\pi r^{2}").move_to(area[1])
        self.play(Write(area))
        self.wait(2)
        self.play(area2.animate.move_to(formula2), FadeOut(formula2))

        #coulomb
        formula3 =  MathTex(r"\phi=E\cdot 4\pi r^{2}").shift(UP*3)
        coulomb = MathTex(r"E=\frac{1}{4\pi \varepsilon_{0}} \cdot \frac{q}{r^{2}}").to_corner(UR)
        solution = MathTex(r"\phi=\frac{q}{\varepsilon_{0}}").shift(UP*3)

        self.wait(4)
        self.play(FadeOut(VGroup(area2, e_con, area)), FadeIn(formula3))
        self.wait(2)
        self.play(Write(coulomb))
        self.wait(7)
        self.play(ReplacementTransform(formula3,solution))
        self.wait(4)

        #show flux
        vecField1Func1 = lambda pos: pos[0]*RIGHT + pos[1]*UP
        colors1 = [ORANGE,RED]
        stream = StreamLines(vecField1Func1, stroke_width=2, max_anchors_per_line=50, virtual_time=50, n_repeats=1, colors=colors1, min_color_scheme_value=1,  max_color_scheme_value=6).set_z_index(-99)

        self.play(FadeOut(coulomb))
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=4)
        self.wait(4)

        #open sphere
        sphere2 = Sphere(u_range=[0,PI], v_range=[PI/2,PI]).rotate(PI/4,axis=RIGHT).scale(2.5).move_to([0,-0.1,0])
        sphere2.rotate(PI, axis=UP)
        self.play(Create(sphere2), FadeOut(sphere), FadeIn(proton))

        #change charge
        core1 = Circle(radius=0.4,color=PURE_GREEN,fill_color=PURE_GREEN,fill_opacity=1)
        corss3 = Rectangle(height=0.03,width=0.3,fill_opacity=1)
        electron = VGroup(core1,corss3)

        self.play(FadeOut(proton), FadeIn(electron))

        stream.end_animation()
        self.remove(stream)

        vecField1Func2 = lambda pos: -pos[0]*RIGHT + -pos[1]*UP
        colors2 = [GREEN,PURE_GREEN]
        stream2 = StreamLines(vecField1Func2, stroke_width=2, max_anchors_per_line=50, virtual_time=50, n_repeats=1, colors=colors2, min_color_scheme_value=1,  max_color_scheme_value=6).set_z_index(-99)
        self.add(stream2)
        stream2.start_animation(warm_up=True, flow_speed=2)
        self.wait(8)

class GaussSurfaceIndependence(Scene):
    def construct(self):

        def vector_field(pos,q=1):
            x, y, _ = pos
            return np.array([
                np.sin(q*(x+4.3)+q*(y+12.8)),
                np.cos(q*(x+4.3)-q*(y+12.8)),
                0
            ])
        def vector_field2(pos,q=1):
            x, y, _ = pos
            return q*np.array([
                x+y,
                y,
                0
            ])
        
        dt = 4

        def flow_function(p):
            return p + dt * vector_field(8*p,0.18)
        def flow_function2(p):
            return p + dt * vector_field2(p,1)

        square = Circle(color=BLUE).set_z_index(-1)
        square2 = Star(color=BLUE, n=10).set_z_index(-1)
        square.set_fill(BLUE, opacity=0.4)
        square2.set_fill(BLUE, opacity=0.4)

        core = Circle(radius=0.4,color=RED,fill_opacity=1)
        corss1 = Rectangle(height=0.02,width=0.4,fill_opacity=1)
        corss2 = Rectangle(height=0.4,width=0.02,fill_opacity=1)
        proton = VGroup(core,corss1,corss2)

        #init
        self.wait()

        self.play(Write(square))
        self.play(Write(proton))

        #field stretch
        func0 = lambda pos: pos[0]*RIGHT + pos[1]*UP
        f0 = ArrowVectorField(func=func0,color=RED).set_opacity(0.7).set_z_index(-2)

        self.play(Create(f0))
        self.play(
            square.animate.apply_function(flow_function),
            run_time=17,
            rate_func=linear
        )

        #2nd example
        self.play(FadeOut(square))
        self.play(Write(square2))
        self.play(
            square2.animate.apply_function(flow_function2),
            run_time=17,
            rate_func=linear
        )

class GaussSurfaceIndependence3D(ThreeDScene):
    def construct(self):

        def vector_field(pos,q=1):
            x, y, z = pos
            return np.array([
                np.sin(q*(x+4.3)+q*(y+12.8)),
                np.cos(q*(x+4.3)-q*(y+12.8)),
                0.1*z
            ])
        def vector_field2(pos,q=1):
            x, y, z = pos
            return q*np.array([
                x+y,
                y,
                -0.1*z
            ])
        
        dt = 4

        def flow_function(p):
            return p + dt * vector_field(8*p,0.18)
        def flow_function2(p):
            return p + dt * vector_field2(p,1)

        square = Sphere(color=BLUE)
        square2 = Sphere(color=BLUE)
        square.set_fill(BLUE, opacity=0.4)
        square2.set_fill(BLUE, opacity=0.4)

        core = Circle(radius=0.4,color=RED,fill_opacity=1)
        corss1 = Rectangle(height=0.02,width=0.4,fill_opacity=1)
        corss2 = Rectangle(height=0.4,width=0.02,fill_opacity=1)
        proton = VGroup(core,corss1,corss2)

        #init
        self.wait()
        self.play(Write(square))
        self.play(Write(proton))
        self.move_camera(phi=60*DEGREES,theta=-45*DEGREES)


        #field stretch
        func0 = lambda pos: pos[0]*RIGHT + pos[1]*UP
        f0 = ArrowVectorField(func=func0,color=RED, x_range=[-10,10], y_range=[-10,10]).set_opacity(0.7).set_z_index(-2)

        self.begin_ambient_camera_rotation(rate=0.3)
        self.play(Create(f0))
        self.play(
            square.animate.apply_function(flow_function),
            run_time=17,
            rate_func=linear
        )

        #2nd example
        self.play(FadeOut(square))
        self.play(Write(square2))
        self.play(
            square2.animate.apply_function(flow_function2),
            run_time=17,
            rate_func=linear
        )

class FaradayIntuition(ThreeDScene):
    def construct(self):

        # 
        # setup tex
        # 
        law_tex = Tex("Faradaysches Induktionsgesetz")
        int_tex = Tex("Integrale Form:").shift(UP*0.5).to_edge(LEFT)
        dif_tex = Tex("Differentielle Form:").shift(UP*3).to_edge(LEFT)
        word_tex = Tex("Wortform:").shift(UP*-2).to_edge(LEFT)
        differential_form = MathTex(r" \nabla \times \vec{E}=-\frac{\partial \vec{B}}{\partial t}").shift(UP*2).to_edge(LEFT)
        integral_form = MathTex(r"\oint_{\partial A}^{}\vec{E}\cdot d\vec{l}=-\frac{d}{dt}\int_{A}^{}\vec{B}\cdot d\vec{A}").shift(UP*-0.5).to_edge(LEFT)
        word_form = Tex("Änderungen des magnetischen Feldes führen zu einem elektrischen Wirbelfeld.").shift(UP*-3).scale(0.8).to_edge(LEFT)
        # 
        # setup tex
        # setup view
        # 
        func1 = lambda pos: vecField1(pos=pos)
        def vecField1(pos):
            e = 0.001
            s = 0.2
            x = pos[0]
            y = pos[1]
            normal1 = x**2 + (y-s)**2 + e
            normal2 = x**2 + (y+s)**2 + e
            field = [0,0]
            field[0] = (y-s)/(normal1) - (y+s)/(normal2)
            field[1] = (-x)/(normal1) + (x)/(normal2)
            return field[0]*RIGHT + field[1]*UP

        def currentFlow(x, b=1, c=10):
            return (c * x) / ((x**2 + b**2)**2)

        #setup
        north_pole = Prism(dimensions=[2,1,1], fill_color=BLUE, fill_opacity=1).move_to([1,0,0])
        south_pole = Prism(dimensions=[2,1,1], fill_color=RED, fill_opacity=1).move_to([-1,0,0])

                #Bfield
        stream = SVGMobject("Magnetfield.svg", use_svg_cache=False).set_fill(opacity=0).scale(8).set_z_index(-1)
        center = stream.get_center() 
        paths = stream.family_members_with_points()
        distances = [np.linalg.norm(path.get_center() - center) for path in paths]
        max_distance = max(distances)
        for path, dist in zip(paths, distances):
            t = dist / max_distance  # 0 = center, 1 = farthest
            color = color_gradient([BLUE, RED, BLACK], 100)[int(t*99)]
            path.set_stroke(color=color, width=0.6)
        stream = VGroup(*paths).set_z_index(-1)
        magnet = VGroup(north_pole, south_pole, stream).set_z_index(1)

        loop = Circle(radius=2,color=GREEN).rotate(PI/2,UP) 

        #move magnet
        vec1 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,0,2]).rotate(PI/2,OUT)
        vec2 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,2,0]).rotate(PI/2,UP)
        vec3 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,0,-2]).rotate(-PI/2,OUT)
        vec4 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,-2,0]).rotate(-PI/2,UP)
        l1 = Line(start=[0,0,2], end=[0,0,2], color=YELLOW)
        l2 = Line(start=[0,2,0], end=[0,2,0], color=YELLOW)
        l3 = Line(start=[0,0,-2], end=[0,0,-2], color=YELLOW)
        l4 = Line(start=[0,-2,0], end=[0,-2,0], color=YELLOW)
        vec1.add_updater(lambda mob: mob.set_y(currentFlow(magnet.get_x())))
        vec2.add_updater(lambda mob: mob.set_z(-currentFlow(magnet.get_x())))
        vec3.add_updater(lambda mob: mob.set_y(-currentFlow(magnet.get_x())))
        vec4.add_updater(lambda mob: mob.set_z(currentFlow(magnet.get_x())))
        l1.add_updater(lambda mob: mob.become(Line(start=[0,0,2], end=vec1.get_center(), color=YELLOW)))
        l2.add_updater(lambda mob: mob.become(Line(start=[0,2,0], end=vec2.get_center(), color=YELLOW)))
        l3.add_updater(lambda mob: mob.become(Line(start=[0,0,-2], end=vec3.get_center(), color=YELLOW)))
        l4.add_updater(lambda mob: mob.become(Line(start=[0,-2,0], end=vec4.get_center(), color=YELLOW)))
        vecs = VGroup(vec1,vec2,vec3,vec4, l1,l2,l3,l4)
        # 
        # setup view
        # 

        #setup
        self.wait()
        self.add_fixed_in_frame_mobjects(law_tex)
        self.play(Write(law_tex))
        self.play(law_tex.animate.to_corner(UR))

        self.play(FadeIn(magnet))
        self.move_camera(phi=60*DEGREES, theta=-45*DEGREES)
        self.play(Write(loop))
        self.play(magnet.animate.move_to([-4,0,0]))
        self.move_camera(frame_center=[-4,-4,-0.2], zoom=0.8)

        #formulas
        self.add_fixed_in_frame_mobjects(dif_tex)
        self.play(Write(dif_tex))
        self.wait()
        self.add_fixed_in_frame_mobjects(differential_form)
        self.play(Write(differential_form))
        self.wait()

        #magnet
        self.add(vecs)
        self.play(magnet.animate.move_to([4,0,0]), rate_func=linear, run_time=5)
        self.play(magnet.animate.move_to([-4,0,0]), rate_func=linear, run_time=5)

        #more formulas
        self.add_fixed_in_frame_mobjects(int_tex)
        self.play(Write(int_tex))
        self.wait()
        self.add_fixed_in_frame_mobjects(integral_form)
        self.play(Write(integral_form))
        self.wait(6)
        self.add_fixed_in_frame_mobjects(word_tex)
        self.play(Write(word_tex))
        self.wait()
        self.add_fixed_in_frame_mobjects(word_form)
        self.play(Write(word_form))
        self.wait()

class FaradayInductionEField(ThreeDScene):
    def construct(self):

        def vecField1(pos):
            e = 0.001
            s = 0.2
            x = pos[0]
            y = pos[1]
            normal1 = x**2 + (y-s)**2 + e
            normal2 = x**2 + (y+s)**2 + e
            field = [0,0]
            field[0] = (y-s)/(normal1) - (y+s)/(normal2)
            field[1] = (-x)/(normal1) + (x)/(normal2)
            return field[0]*RIGHT + field[1]*UP

        def vecField2(pos):
            r = 0.6
            b = 5
            e = 0.1
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = -b*y/(x**2 + y**2 + e) 
            field[1] = b*x/(x**2 + y**2 + e)
            if field[0]**2 + field[1]**2 < r:
                return 0*RIGHT + 0*UP
            else:
                return field[0]*RIGHT + field[1]*UP

        def currentFlow(x, b=1, c=10):
            return -(c * x) / ((x**2 + b**2)**2)

        #setup
        north_pole = Prism(dimensions=[2,1,1], fill_color=BLUE, fill_opacity=1).move_to([1,0,0])
        south_pole = Prism(dimensions=[2,1,1], fill_color=RED, fill_opacity=1).move_to([-1,0,0])
        func1 = lambda pos: vecField1(pos=pos)
                #Bfield
        stream = SVGMobject("Magnetfield.svg", use_svg_cache=False).set_fill(opacity=0).scale(8).set_z_index(-1)
        center = stream.get_center() 
        paths = stream.family_members_with_points()
        distances = [np.linalg.norm(path.get_center() - center) for path in paths]
        max_distance = max(distances)
        for path, dist in zip(paths, distances):
            t = dist / max_distance  # 0 = center, 1 = farthest
            color = color_gradient([BLUE, RED, BLACK], 100)[int(t*99)]
            path.set_stroke(color=color, width=0.6)
        stream = VGroup(*paths).set_z_index(-1)
        magnet = VGroup(north_pole, south_pole, stream).set_z_index(1)


        self.move_camera(phi=60*DEGREES, theta=-45*DEGREES)
        self.play(FadeIn(magnet))
        self.wait(2)

        #efield
        colors1 = [BLUE, YELLOW, YELLOW, ORANGE, ORANGE, RED]
        vecField1Func1 = lambda pos: vecField2(pos=pos)
        vecField1Func2 = lambda pos: vecField2(pos=-pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=3.2,min_color_scheme_value=0.8, colors=colors1, x_range=[-6,6], y_range=[-6,6]).rotate(PI/2, UP)
        vector_field2 = ArrowVectorField(vecField1Func2, max_color_scheme_value=3.2,min_color_scheme_value=0.8, colors=colors1, x_range=[-6,6], y_range=[-6,6]).rotate(PI/2, UP)

        #move magnet
        self.play(magnet.animate.move_to([-4,0,0]), run_time=2)
        self.wait(3)
        vector_field1.add_updater(lambda mob, dt: mob.rotate(0.3*dt*currentFlow(magnet.get_x()), RIGHT))
        vector_field2.add_updater(lambda mob, dt: mob.rotate(0.3*dt*currentFlow(magnet.get_x()), RIGHT))

        self.add(vector_field1)
        self.play(magnet.animate.move_to([0,0,0]), rate_func=linear, run_time=6)
        self.add(vector_field2)
        self.remove(vector_field1)
        self.play(magnet.animate.move_to([4,0,0]), rate_func=linear, run_time=6)
        self.remove(vector_field2)

        self.wait(2)
        self.play(magnet.animate.move_to([-4,0,0]),run_time=2.5)
        self.add(vector_field1)
        self.play(magnet.animate.move_to([0,0,0]), rate_func=linear, run_time=6)
        self.add(vector_field2)
        self.remove(vector_field1)
        self.play(magnet.animate.move_to([4,0,0]), rate_func=linear, run_time=6)
        self.remove(vector_field2)

        self.wait(2)
        self.play(magnet.animate.move_to([-4,0,0]),run_time=2.5)
        self.add(vector_field1)
        self.play(magnet.animate.move_to([0,0,0]), rate_func=linear, run_time=6)
        self.add(vector_field2)
        self.remove(vector_field1)
        self.play(magnet.animate.move_to([4,0,0]), rate_func=linear, run_time=6)
        self.remove(vector_field2)

        self.wait(4)

        #numberplanes
        n1 = NumberPlane(x_length=7, y_length=7, x_range=[-3.5,3.5], y_range=[-3.5,3.5]).rotate(PI/2, UP).shift(LEFT*6)
        n2 = NumberPlane(x_length=7, y_length=7, x_range=[-3.5,3.5], y_range=[-3.5,3.5]).rotate(PI/2, UP).shift(LEFT*4)
        n3 = NumberPlane(x_length=7, y_length=7, x_range=[-3.5,3.5], y_range=[-3.5,3.5]).rotate(PI/2, UP).shift(LEFT*2)
        n4 = NumberPlane(x_length=7, y_length=7, x_range=[-3.5,3.5], y_range=[-3.5,3.5]).rotate(PI/2, UP).shift(LEFT*0)
        n5 = NumberPlane(x_length=7, y_length=7, x_range=[-3.5,3.5], y_range=[-3.5,3.5]).rotate(PI/2, UP).shift(LEFT*-2)
        n6 = NumberPlane(x_length=7, y_length=7, x_range=[-3.5,3.5], y_range=[-3.5,3.5]).rotate(PI/2, UP).shift(LEFT*-4)
        n7 = NumberPlane(x_length=7, y_length=7, x_range=[-3.5,3.5], y_range=[-3.5,3.5]).rotate(PI/2, UP).shift(LEFT*-6)

        self.play(AnimationGroup(FadeIn(n1),FadeIn(n2),FadeIn(n3),FadeIn(n4),FadeIn(n5),FadeIn(n6),FadeIn(n7), lag_ratio=1))
        self.wait()

class ChargesInFields(Scene):
    def construct(self):

        def vecField1(pos):
            b = 5
            e = 0.1
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = -b*y/(x**2 + y**2 + e) 
            field[1] = b*x/(x**2 + y**2 + e)
            return field[0]*RIGHT + field[1]*UP

        #fields
        colors1 = [BLUE, YELLOW, YELLOW, ORANGE, ORANGE, RED]
        vecField1Func1 = lambda pos: vecField1(pos=pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=3.2,min_color_scheme_value=0.8, colors=colors1).set_z_index(-1)

        class MagnetIn(VGroup):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                point = Dot().scale(1)
                circle = Circle(color=WHITE,radius=0.3)
                self.point = point
                self.circle = circle
                self.add(point,circle)

        magnetIn1 = MagnetIn()
        # magnetIn1 = MagnetIn().shift(LEFT*1)
        magnetIn2 = MagnetIn().scale(2).shift(LEFT*2)
        magnetIn3 = MagnetIn().scale(4).shift(LEFT*4)
        magnetIn4 = MagnetIn().scale(4).shift(LEFT*-4)

        allMagnets = VGroup(magnetIn1)
        # allMagnets = VGroup(magnetIn1,magnetIn2,magnetIn3,magnetIn4)

        self.wait()
        self.play(Write(vector_field1))
        self.wait(3)
        self.play(FadeIn(allMagnets))

        #moving chrages
        core = Circle(radius=0.4,color=RED,fill_opacity=1)
        corss1 = Rectangle(height=0.02,width=0.4,fill_opacity=1)
        corss2 = Rectangle(height=0.4,width=0.02,fill_opacity=1)
        proton = VGroup(core,corss1,corss2).shift(LEFT*2).scale(0.7)

        core1 = Circle(radius=0.4,color=PURE_GREEN,fill_color=PURE_GREEN,fill_opacity=1)
        corss3 = Rectangle(height=0.03,width=0.3,fill_opacity=1)
        electron = VGroup(core1,corss3).shift(RIGHT*2).scale(0.7)

        self.wait(4)
        self.play(Write(proton), Write(electron))
        self.wait()
        self.play(Rotate(proton, PI, about_point=ORIGIN), Rotate(electron, -PI, about_point=ORIGIN), rate_func=linear, run_time=5)
        self.play(Rotate(proton, PI, about_point=ORIGIN), Rotate(electron, -PI, about_point=ORIGIN), rate_func=linear, run_time=5)
        self.play(Rotate(proton, PI, about_point=ORIGIN), Rotate(electron, -PI, about_point=ORIGIN), rate_func=linear, run_time=5)
        self.play(Rotate(proton, PI, about_point=ORIGIN), Rotate(electron, -PI, about_point=ORIGIN), rate_func=linear, run_time=5)
        self.wait()

class FaradayInductionCharges(ThreeDScene):
    def construct(self):

        func1 = lambda pos: vecField1(pos=pos)
        def vecField1(pos):
            e = 0.001
            s = 0.2
            x = pos[0]
            y = pos[1]
            normal1 = x**2 + (y-s)**2 + e
            normal2 = x**2 + (y+s)**2 + e
            field = [0,0]
            field[0] = (y-s)/(normal1) - (y+s)/(normal2)
            field[1] = (-x)/(normal1) + (x)/(normal2)
            return field[0]*RIGHT + field[1]*UP

        def currentFlow(x, b=1, c=10):
            return -(c * x) / ((x**2 + b**2)**2)

        #setup
        north_pole = Prism(dimensions=[2,1,1], fill_color=BLUE, fill_opacity=1).move_to([1,0,0])
        south_pole = Prism(dimensions=[2,1,1], fill_color=RED, fill_opacity=1).move_to([-1,0,0])

                #Bfield
        stream = SVGMobject("Magnetfield.svg", use_svg_cache=False).set_fill(opacity=0).scale(8).set_z_index(-1)
        center = stream.get_center() 
        paths = stream.family_members_with_points()
        distances = [np.linalg.norm(path.get_center() - center) for path in paths]
        max_distance = max(distances)
        for path, dist in zip(paths, distances):
            t = dist / max_distance  # 0 = center, 1 = farthest
            color = color_gradient([BLUE, RED, BLACK], 100)[int(t*99)]
            path.set_stroke(color=color, width=0.6)
        stream = VGroup(*paths).set_z_index(-1)
        magnet = VGroup(north_pole, south_pole, stream).set_z_index(1)

        magnet = VGroup(north_pole, south_pole, stream).set_z_index(1)

        loop = Circle(radius=2,color=GREEN).rotate(PI/2,UP) 

        self.wait()
        self.play(FadeIn(magnet))
        self.wait()
        self.move_camera(phi=60*DEGREES, theta=-45*DEGREES)
        self.wait()
        self.play(Write(loop))
        self.wait(5)
        
        self.play(magnet.animate.move_to([-4,0,0]), run_time=2)

        #move magnet
        vec1 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,0,2]).rotate(PI/2,OUT)
        vec2 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,2,0]).rotate(PI/2,UP)
        vec3 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,0,-2]).rotate(-PI/2,OUT)
        vec4 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,-2,0]).rotate(-PI/2,UP)
        l1 = Line(start=[0,0,2], end=[0,0,2], color=YELLOW)
        l2 = Line(start=[0,2,0], end=[0,2,0], color=YELLOW)
        l3 = Line(start=[0,0,-2], end=[0,0,-2], color=YELLOW)
        l4 = Line(start=[0,-2,0], end=[0,-2,0], color=YELLOW)
        vec1.add_updater(lambda mob: mob.set_y(currentFlow(magnet.get_x())))
        vec2.add_updater(lambda mob: mob.set_z(-currentFlow(magnet.get_x())))
        vec3.add_updater(lambda mob: mob.set_y(-currentFlow(magnet.get_x())))
        vec4.add_updater(lambda mob: mob.set_z(currentFlow(magnet.get_x())))
        l1.add_updater(lambda mob: mob.become(Line(start=[0,0,2], end=vec1.get_center(), color=YELLOW)))
        l2.add_updater(lambda mob: mob.become(Line(start=[0,2,0], end=vec2.get_center(), color=YELLOW)))
        l3.add_updater(lambda mob: mob.become(Line(start=[0,0,-2], end=vec3.get_center(), color=YELLOW)))
        l4.add_updater(lambda mob: mob.become(Line(start=[0,-2,0], end=vec4.get_center(), color=YELLOW)))
        vecs = VGroup(vec1,vec2,vec3,vec4, l1,l2,l3,l4)

        self.wait(2)
        self.add(vecs)
        self.play(FadeIn(vecs))
        self.play(magnet.animate.move_to([4,0,0]), rate_func=linear, run_time=7)
        self.play(magnet.animate.move_to([-4,0,0]), rate_func=linear, run_time=7)
        self.play(magnet.animate.move_to([4,0,0]), rate_func=linear, run_time=7)
        self.play(magnet.animate.move_to([-4,0,0]), rate_func=linear, run_time=7)
        self.play(magnet.animate.move_to([4,0,0]), rate_func=linear, run_time=7)
        self.play(magnet.animate.move_to([-4,0,0]), rate_func=linear, run_time=7)
        self.wait()

class CurlIntro(Scene):
    def construct(self):

        def vecField1(pos):
            e = 0.001
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = -y
            field[1] = x
            return field[0]*RIGHT + field[1]*UP

        def vecField2(pos):
            e = 0.001
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = y
            field[1] = -x
            return field[0]*RIGHT + field[1]*UP

        def curlFunc1(x,y):
            return 2

        def curlFunc2(x,y):
            return -2

        colors1 = [BLUE,GREEN,YELLOW,RED]
        vecField1Func1 = lambda pos: vecField1(pos=pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=8,min_color_scheme_value=1, colors=colors1).set_z_index(-1)

        rot = Tex("Rotation").scale(2).to_edge(UP)
        b1 = SurroundingRectangle(rot,color=BLACK,fill_color=BLACK,fill_opacity=0.7, stroke_opacity=0).move_to(rot)

        stream = StreamLines(vecField1Func1, stroke_width=2, max_color_scheme_value=8)

        #basic shwow
        self.wait()
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=1)
        self.wait(2)
        self.play(FadeIn(VGroup(b1,rot)))
        self.wait(4)
        self.play(FadeOut(stream))
        stream.end_animation()
        self.remove(stream)

        #vector field and quantity
        p1 = Dot().scale(0.5)
        c1 = Circle(color=WHITE,radius=0.2).shift(UP)
        rot_tex = MathTex(r"rot\vec{F}=")
        rot_tex[0][3:5].set_color(YELLOW)
        decnum = DecimalNumber(2)
        s1 = SurroundingRectangle(rot_tex,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)
        s2 = SurroundingRectangle(decnum,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)

        p1.add_updater(lambda mob: mob.move_to(c1))
        rot_tex.add_updater(lambda mob: mob.next_to(c1,UP))
        s1.add_updater(lambda mob: mob.move_to(rot_tex))
        s2.add_updater(lambda mob: mob.move_to(decnum))
        decnum.add_updater(lambda mob: mob.set_value(curlFunc1(p1.get_x(),p1.get_y())).next_to(c1,UP).shift(RIGHT*1.5))

        #setup
        self.play(Write(vector_field1))
        self.wait()
        self.add(p1,s1,s2,decnum,c1,rot_tex)

        #show uniform
        self.play(c1.animate.move_to([0,0,0]))
        self.wait()
        self.play(c1.animate.move_to([2,0,0]), run_time=2)
        self.wait()
        self.play(c1.animate.move_to([5,0,0]), run_time=2)
        self.wait()
        self.play(c1.animate.move_to([3,-2,0]), run_time=2)
        self.wait()
        self.play(c1.animate.move_to([0,-3,0]), run_time=2)
        self.wait()
        self.play(c1.animate.move_to([0,0,0]), run_time=2)
        self.wait()

        #old dir
        vecField1Func2 = lambda pos: vecField2(pos=pos)
        vector_field2 = ArrowVectorField(vecField1Func2, max_color_scheme_value=8,min_color_scheme_value=1, colors=colors1).set_z_index(-1)
        stream2 = StreamLines(vecField1Func1, stroke_width=2, color=BLUE)
        stream3 = StreamLines(vecField1Func2, stroke_width=2, color=BLUE)

        self.add(stream2)
        stream2.start_animation(warm_up=True, flow_speed=1)
        self.wait(3)
        self.play(FadeOut(stream2))
        self.wait(2)

        #dir change
        self.play(vector_field1.animate.become(vector_field2))

        decnum.clear_updaters()
        decnum.add_updater(lambda mob: mob.set_value(curlFunc2(p1.get_x(),p1.get_y())).next_to(c1,UP).shift(RIGHT*1.5))

        self.add(stream3)
        stream3.start_animation(warm_up=True, flow_speed=1)
        self.wait(6)
        self.play(FadeOut(stream3))
        self.remove(stream2,stream3)
        self.wait()

class CurlComplexExample(Scene):
    def construct(self):

        def vecField3(pos):
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = np.sin(0.5*(x+y))
            field[1] = np.cos(0.5*(x-y))
            return field[0]*RIGHT + field[1]*UP

        def curlFunc3(x,y):
            xcomp = np.sin(0.5*x - 0.5*y)
            ycomp = np.cos(0.5*x + 0.5*y)
            return -0.5*(xcomp + ycomp)

        colors1 = [BLUE,GREEN,YELLOW,RED]
        vecField1Func1 = lambda pos: vecField3(pos=pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=1.4,min_color_scheme_value=0.5, colors=colors1).set_z_index(-1)
        stream = StreamLines(vecField1Func1, stroke_width=2, max_color_scheme_value=1.4, min_color_scheme_value=0.5)

        #basic shwow
        self.wait()
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=1)
        self.wait(10)

        #vector field and quantity
        p1 = Dot().scale(0.5)
        c1 = Circle(color=WHITE,radius=0.2).shift(UP)
        rot_tex = MathTex(r"rot\vec{F}=")
        rot_tex[0][3:5].set_color(YELLOW)
        decnum = DecimalNumber(2)
        s1 = SurroundingRectangle(rot_tex,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)
        s2 = SurroundingRectangle(decnum,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)

        p1.add_updater(lambda mob: mob.move_to(c1))
        rot_tex.add_updater(lambda mob: mob.next_to(c1,UP))
        s1.add_updater(lambda mob: mob.move_to(rot_tex))
        s2.add_updater(lambda mob: mob.move_to(decnum))
        decnum.add_updater(lambda mob: mob.set_value(curlFunc3(p1.get_x(),p1.get_y())).next_to(c1,UP).shift(RIGHT*1.5))

        #setup
        self.play(Write(vector_field1))
        self.wait()
        self.play(FadeOut(stream))
        stream.end_animation()
        self.remove(stream)
        self.wait()

        self.add(p1,s1,s2,decnum,c1,rot_tex)
        #show uniform
        self.play(c1.animate.move_to([0,0,0]))
        self.wait(2)
        self.play(c1.animate.move_to([-5,0,0]))
        self.wait(1)
        self.play(c1.animate.move_to([0,2,0]))
        self.wait(1)
        self.play(c1.animate.move_to([-3,-1,0]))
        self.wait(1)
        self.play(c1.animate.move_to([0,0,0]))
        self.wait(1)

        #clear prepare twig
        self.remove(p1,s1,s2,decnum,c1,rot_tex)
        
        branch1 = Rectangle(width=1.3, height=0.13, fill_color=GRAY_B, color=BLACK, fill_opacity=1)
        branch2 = Rectangle(width=1.3, height=0.13, fill_color=WHITE, color=BLACK, fill_opacity=1).rotate(PI/2)
        center = Circle(radius=0.13, fill_opacity=1, color=WHITE)
        twig = VGroup(branch1,branch2,center)

        self.wait(2)
        self.play(Write(twig))
        self.wait(5)

        #show twig at spot
        dt = 0.2
        twig.add_updater(lambda mob: mob.rotate(dt*curlFunc3(twig.get_x(),twig.get_y())))
        self.play(twig.animate.move_to([-4.5,-1.5,0]),rate_func=linear, run_time=6)
        self.wait(3, frozen_frame=False)
        self.play(twig.animate.move_to([2,-1.5,0]),rate_func=linear, run_time=6)
        self.wait(3, frozen_frame=False)
        self.play(twig.animate.move_to([1.5,1.6,0]),rate_func=linear, run_time=6)
        self.wait(3, frozen_frame=False)
        self.play(twig.animate.move_to([-1.5,1.5,0]),rate_func=linear, run_time=6)
        self.wait(5, frozen_frame=False)

class Curl3D(ThreeDScene):
    def construct(self):

        def vecField1(pos):
            r = 37
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = -y
            field[1] = x
            if field[0]**2 + field[1]**2 > r:
                return 0*RIGHT + 0*UP
            else:
                return field[0]*RIGHT + field[1]*UP

        colors1 = [BLUE,GREEN,YELLOW,RED]
        vecField1Func1 = lambda pos: vecField1(pos=pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=6,min_color_scheme_value=1, colors=colors1,
                                         x_range=[-6,6], y_range=[-6,6]).set_z_index(-1)
        
        axis = ThreeDAxes(x_range=[-2,2,1],y_range=[-2,2,1],z_range=[0,0.01,0.01],x_length=12,y_length=12,z_length=0.01,z_axis_config={"include_tip": False})

        ihat = Vector([2,0]).set_color(PURE_RED)
        jhat = Vector([0,2]).set_color(PURE_GREEN)
        khat = Vector([0,0,2]).set_color(PURE_BLUE).set_z_index(99)

        ihat_tex = MathTex(r"\hat{i}").set_color(PURE_RED).move_to([1,-1,0])
        jhat_tex = MathTex(r"\hat{j}").set_color(PURE_GREEN).move_to([1,1,0])
        khat_tex = MathTex(r"\hat{k}").set_color(PURE_BLUE).move_to([-1,0,1]).rotate(PI/2,axis=RIGHT).rotate(PI/2,axis=OUT)

        #intro khat
        self.wait()
        self.play(Write(VGroup(ihat_tex,jhat_tex)), GrowArrow(ihat), GrowArrow(jhat))
        self.wait(3)
        self.move_camera(phi=60*DEGREES, theta=-45*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.move_camera(zoom=2.5,frame_center=[0,0,0.3])

        self.play(Write(khat_tex), GrowArrow(khat), ihat_tex.animate.rotate(PI/2,axis=OUT))
        self.wait(5)

        #vector field
        self.play(FadeIn(axis))
        self.wait(3)
        self.play(FadeIn(vector_field1))
        self.wait(3)
        self.move_camera(zoom=1,frame_center=[0,0,0], theta=PI/4)

        self.stop_ambient_camera_rotation()
        self.play(Rotate(vector_field1, 2*PI), run_time=10)
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.2)

        #streamlines
        stream = StreamLines(vecField1Func1, stroke_width=2, max_anchors_per_line=50, virtual_time=50, n_repeats=1, colors=colors1, min_color_scheme_value=1,  max_color_scheme_value=6).set_z_index(-99)

        self.play(vector_field1.animate.set_opacity(0.2), run_time=1)
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=2)
        self.wait(7)
        self.move_camera(zoom=2)
        self.wait(7)

class CurlToNabla(Scene):
    def construct(self):
        
        rot_tex = MathTex(r"rot", r"\vec{E}").shift(UP+LEFT)
        nabla_tex = MathTex(r"\nabla \times",r"\vec{E}").shift(UP+RIGHT)
        rot_tex[1].set_color(YELLOW)
        nabla_tex[1].set_color(YELLOW)
        
        self.wait()
        self.play(Write(rot_tex))
        self.wait()
        self.play(Write(nabla_tex))
        self.wait(5)
        self.play(VGroup(rot_tex,nabla_tex).animate.to_edge(UP))

        # Show components
        nabla_components = MathTex(r"\nabla=\left [ \frac{\partial}{\partial x},\frac{\partial}{\partial y} \right ]").shift(UP*2)
        self.wait()
        self.play(Write(nabla_components))
        self.wait(6)
        self.play(nabla_components.animate.to_edge(LEFT))

        equation = MathTex(r"\nabla \times \vec{E} = \frac{\partial}{\partial x} E_{y} - \frac{\partial}{\partial y} E_{x}").to_edge(LEFT)
        self.wait(3)
        self.play(Write(equation))

        #cross product
        i_hat = Vector([-1,-1], color=RED)
        j_hat = Vector([2,0], color=GREEN)
        k_hat = Vector([0,2], color=BLUE)
        vecs = VGroup(i_hat,j_hat,k_hat).shift(RIGHT*2)

        cross_equation = MathTex(r"\hat{i} \times",r"\hat{j}",r"=",r"\hat{k}").shift(RIGHT*3+DOWN*2)
        cross_equation[0][0:2].set_color(RED)
        cross_equation[1].set_color(GREEN)
        cross_equation[3].set_color(BLUE)

        self.wait(6)
        self.play(Write(vecs))
        self.wait()
        self.play(Write(cross_equation))
        self.wait(12)

        equation2 = MathTex(r"\nabla \cdot \vec{E} = \frac{\partial}{\partial x} E_{x} + \frac{\partial}{\partial y} E_{y}").shift(DOWN*2).to_edge(LEFT)
        self.play(Write(equation2))
        self.wait()

class FaradayCurl(Scene):
    def construct(self):

        def vecField1(pos):
            b = 5
            e = 0.1
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = -b*y/(x**2 + y**2 + e) 
            field[1] = b*x/(x**2 + y**2 + e)
            return field[0]*RIGHT + field[1]*UP

        def vecField2(pos):
            b = 5
            e = 0.1
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = b*y/(x**2 + y**2 + e) 
            field[1] = -b*x/(x**2 + y**2 + e)
            return field[0]*RIGHT + field[1]*UP

        def curlField1(x,y):
            e=0.0001
            return 2*5*0.1/(x**2 + y**2 + 0.1)

        def curlField2(x,y):
            e=0.0001
            return -2*5*0.1/(x**2 + y**2 + 0.1)


        p1 = Dot().scale(0.5)
        c1 = Circle(color=WHITE,radius=0.25)
        div_tex = MathTex(r" \nabla \times \vec{E}=")
        div_tex[0][2:4].set_color(YELLOW)
        decnum = DecimalNumber(0)
        decnum2 = DecimalNumber(0)
        s1 = SurroundingRectangle(div_tex,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)
        s2 = SurroundingRectangle(decnum,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)
        s3 = SurroundingRectangle(decnum2,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)

        c1.add_updater(lambda mob: mob.move_to(p1))
        div_tex.add_updater(lambda mob: mob.next_to(c1,UP))
        s1.add_updater(lambda mob: mob.move_to(div_tex))
        s2.add_updater(lambda mob: mob.move_to(decnum))
        s3.add_updater(lambda mob: mob.move_to(decnum2))
        decnum.add_updater(lambda mob: mob.next_to(c1,UP).shift(RIGHT*1.5).set_value(curlField1(c1.get_x(),c1.get_y())))
        decnum2.add_updater(lambda mob: mob.next_to(c1,UP).shift(RIGHT*1.5).set_value(curlField2(c1.get_x(),c1.get_y())))

        #fields
        colors1 = [BLUE, YELLOW, YELLOW, ORANGE, ORANGE, RED]
        vecField1Func1 = lambda pos: vecField1(pos=pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=3.2,min_color_scheme_value=0.8, colors=colors1).set_z_index(-1)
        stream = StreamLines(vecField1Func1, stroke_width=2, max_anchors_per_line=100, virtual_time=5, n_repeats=1, max_color_scheme_value=3.2, min_color_scheme_value=0.8).set_z_index(-1)

        p2 = Dot().scale(1)
        c2 = Circle(color=WHITE,radius=0.3)
        magnetIn = VGroup(p2,c2)

        self.wait()
        self.play(Write(magnetIn))
        self.wait()
        self.play(Write(vector_field1))
        self.add(stream)
        stream.start_animation(flow_speed=0.7)
        self.wait(3,frozen_frame=False)


        #show curl change
        self.add(p1,s1,s2,decnum,c1,div_tex)
        self.play(p1.animate.move_to([1,0,0]), run_time=3)
        self.wait(frozen_frame=False)
        self.play(p1.animate.move_to([2,0,0]), run_time=3)
        self.wait(frozen_frame=False)
        self.play(p1.animate.move_to([3,1,0]), run_time=3)
        self.wait(frozen_frame=False)
        self.play(p1.animate.move_to([-3,-2,0]), run_time=6)
        self.wait(2,frozen_frame=False)
        self.play(p1.animate.move_to([0,0,0]), run_time=3)
        self.wait(4,frozen_frame=False)

        #reverse curl
        vecField1Func2 = lambda pos: vecField2(pos=pos)
        vector_field2 = ArrowVectorField(vecField1Func2, max_color_scheme_value=3.2,min_color_scheme_value=0.8, colors=colors1).set_z_index(-1)
        stream2 = StreamLines(vecField1Func2, stroke_width=2, max_anchors_per_line=100, virtual_time=5, n_repeats=1, max_color_scheme_value=3.2, min_color_scheme_value=0.8).set_z_index(-1)

        r1 = Rectangle(width=0.52, height=0.02, color=WHITE, fill_opacity=1).rotate(PI/4)
        r2 = Rectangle(width=0.52, height=0.02, color=WHITE, fill_opacity=1).rotate(-PI/4)
        c3 = Circle(color=WHITE,radius=0.3)
        magnetOut = VGroup(r1, r2 ,c3)

        self.play(FadeOut(stream))
        self.remove(stream)
        self.play(ReplacementTransform(magnetIn,magnetOut))
        self.play(vector_field1.animate.become(vector_field2))
        self.add(stream2)
        stream2.start_animation(flow_speed=0.7)
        self.wait(4,frozen_frame=False)

        self.remove(decnum,s2)
        self.add(s3,decnum2)

        self.play(p1.animate.move_to([-2,0,0]), run_time=3)
        self.wait(frozen_frame=False)
        self.play(p1.animate.move_to([-1,-1,0]), run_time=3)
        self.wait(frozen_frame=False)

class FaradayDiffForm(ThreeDScene):
    def construct(self):

        def vecField1(pos):
            e = 0.001
            s = 0.2
            x = pos[0]
            y = pos[1]
            normal1 = x**2 + (y-s)**2 + e
            normal2 = x**2 + (y+s)**2 + e
            field = [0,0]
            field[0] = (y-s)/(normal1) - (y+s)/(normal2)
            field[1] = (-x)/(normal1) + (x)/(normal2)
            return field[0]*RIGHT + field[1]*UP

        def vecField2(pos):
            r = 0.6
            b = 5
            e = 0.1
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = -b*y/(x**2 + y**2 + e) 
            field[1] = b*x/(x**2 + y**2 + e)
            if field[0]**2 + field[1]**2 < r:
                return 0*RIGHT + 0*UP
            else:
                return field[0]*RIGHT + field[1]*UP

        def currentFlow(x, b=1, c=10):
            return -(c * x) / ((x**2 + b**2)**2)

        #setup
        differential_form = MathTex(r" \nabla \times \vec{E}=-\frac{\partial \vec{B}}{\partial t}").to_edge(UP)
        b1 = SurroundingRectangle(differential_form,color=BLACK,fill_color=BLACK,fill_opacity=0.7, stroke_opacity=0).move_to(differential_form)
        self.wait()
        self.add_fixed_in_frame_mobjects(b1,differential_form)
        self.play(Write(differential_form))
        self.play(differential_form.animate.to_corner(UR))

        north_pole = Prism(dimensions=[2,1,1], fill_color=BLUE, fill_opacity=1).move_to([1,0,0])
        south_pole = Prism(dimensions=[2,1,1], fill_color=RED, fill_opacity=1).move_to([-1,0,0])
        func1 = lambda pos: vecField1(pos=pos)
                #Bfield
        stream = SVGMobject("Magnetfield.svg", use_svg_cache=False).set_fill(opacity=0).scale(8).set_z_index(-1)
        center = stream.get_center() 
        paths = stream.family_members_with_points()
        distances = [np.linalg.norm(path.get_center() - center) for path in paths]
        max_distance = max(distances)
        for path, dist in zip(paths, distances):
            t = dist / max_distance  # 0 = center, 1 = farthest
            color = color_gradient([BLUE, RED, BLACK], 100)[int(t*99)]
            path.set_stroke(color=color, width=1.1)
        stream = VGroup(*paths).set_z_index(-1)
        magnet = VGroup(north_pole, south_pole, stream).set_z_index(1)

        self.wait(5)
        self.move_camera(phi=60*DEGREES, theta=-45*DEGREES)
        self.play(FadeIn(magnet))

        #efield
        colors1 = [BLUE, YELLOW, YELLOW, ORANGE, ORANGE, RED]
        vecField1Func1 = lambda pos: vecField2(pos=pos)
        vecField1Func2 = lambda pos: vecField2(pos=-pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=3.2,min_color_scheme_value=0.8, colors=colors1, x_range=[-6,6], y_range=[-6,6]).rotate(PI/2, UP)
        vector_field2 = ArrowVectorField(vecField1Func2, max_color_scheme_value=3.2,min_color_scheme_value=0.8, colors=colors1, x_range=[-6,6], y_range=[-6,6]).rotate(PI/2, UP)

        #move magnet
        self.play(magnet.animate.move_to([-4,0,0]), run_time=1.5)
        vector_field1.add_updater(lambda mob, dt: mob.rotate(0.3*dt*currentFlow(magnet.get_x()), RIGHT))
        vector_field2.add_updater(lambda mob, dt: mob.rotate(0.3*dt*currentFlow(magnet.get_x()), RIGHT))

        #move magnet
        self.add(vector_field1)
        self.play(magnet.animate.move_to([0,0,0]), rate_func=linear, run_time=6)
        self.add(vector_field2)
        self.remove(vector_field1)
        self.play(magnet.animate.move_to([4,0,0]), rate_func=linear, run_time=6)
        self.remove(vector_field2)

        self.wait(2)
        self.play(magnet.animate.move_to([-4,0,0]),run_time=2.5)
        self.add(vector_field1)
        self.play(magnet.animate.move_to([0,0,0]), rate_func=linear, run_time=6)
        self.add(vector_field2)
        self.remove(vector_field1)
        self.play(magnet.animate.move_to([4,0,0]), rate_func=linear, run_time=6)
        self.remove(vector_field2)

        self.wait(2)
        self.play(magnet.animate.move_to([-4,0,0]),run_time=2.5)
        self.add(vector_field1)
        self.play(magnet.animate.move_to([0,0,0]), rate_func=linear, run_time=6)
        self.add(vector_field2)
        self.remove(vector_field1)
        self.play(magnet.animate.move_to([4,0,0]), rate_func=linear, run_time=6)
        self.remove(vector_field2)

        self.play(magnet.animate.move_to([0,0,0]), rate_func=linear, run_time=3)

        #camera change in B
        self.move_camera(phi=0, theta=PI/2)

        loop = Circle(radius=2,color=GREEN).rotate(PI/2,UP) 
        self.play(FadeIn(loop))
        self.play(magnet.animate.move_to([3,0,0]), rate_func=linear, run_time=3)
        self.play(magnet.animate.move_to([-3,0,0]), rate_func=linear, run_time=3)
        self.play(magnet.animate.move_to([1,0,0]), rate_func=linear, run_time=3)
        self.play(magnet.animate.move_to([-1,0,0]), rate_func=linear, run_time=3)
        self.play(magnet.animate.move_to([1,0,0]), rate_func=linear, run_time=3)
        self.play(magnet.animate.move_to([-1,0,0]), rate_func=linear, run_time=3)
        self.play(magnet.animate.move_to([3,0,0]), rate_func=linear, run_time=3)
        self.wait()

class MagneticFlux(ThreeDScene):
    def construct(self):

        positive_plate = Rectangle(height=8,width=0.5,color=RED,fill_opacity=1).shift(LEFT*6 +DOWN*2)
        positive_plate2 = Polygon(positive_plate.get_corner(UR),positive_plate.get_corner(DR),positive_plate.get_corner(DR)+[0.2,0.4,0],positive_plate.get_corner(UR)+[0.2,-0.4,0],fill_opacity=1,color=ManimColor.from_rgb((160,30,30, 1)))
        negativ_plate = Rectangle(height=8,width=0.5,color=GREEN,fill_opacity=1).shift(RIGHT*6+DOWN*2)
        negativ_plate2 = Polygon(negativ_plate.get_corner(UL),negativ_plate.get_corner(DL),negativ_plate.get_corner(DL)+[-0.2,0.4,0],negativ_plate.get_corner(UL)+[-0.2,-0.4,0],fill_opacity=1,color=ManimColor.from_rgb((16,140,16, 1)))

        field_line1 = Arrow([-6,2,0],[6,2,0])
        field_line2 = Arrow([-6,1,0],[6,1,0])
        field_line3 = Arrow([-6,0,0],[6,0,0])
        field_line4 = Arrow([-6,-1,0],[6,-1,0])
        field_line5 = Arrow([-6,-2,0],[6,-2,0])
        field_line6 = Arrow([-6,-3,0],[6,-3,0])
        field_line7 = Arrow([-6,-4,0],[6,-4,0])
        fieldLines = VGroup(field_line1,field_line2,field_line3,field_line4,field_line5,field_line6,field_line7).set_color(YELLOW)

        #condensator fieldlines
        b_field = MathTex(r"\vec{B}").set_color(YELLOW).next_to(positive_plate,UP)

        self.wait()
        self.play(Write(positive_plate),Write(positive_plate2))
        self.wait()
        self.play(Write(negativ_plate), Write(negativ_plate2))
        self.wait()
        self.play(Write(b_field))
        self.wait()
        self.play(AnimationGroup(GrowArrow(fieldLines[0]),GrowArrow(fieldLines[1]),GrowArrow(fieldLines[2]),GrowArrow(fieldLines[3]),GrowArrow(fieldLines[4]),GrowArrow(fieldLines[5]),GrowArrow(fieldLines[6]), lag_ratio=0.7), run_time=5)

        #introduce surface
        plane_surface = Rectangle(height=4,width=0.25,fill_opacity=1,color=BLUE).set_z_index(1)
        plane_surface2 = Polygon(plane_surface.get_corner(UR),plane_surface.get_corner(DR),plane_surface.get_corner(DR)+[0.2,0.4,0],plane_surface.get_corner(UR)+[0.2,-0.4,0],fill_opacity=1,color=DARK_BLUE).set_z_index(-1)

        self.wait(7)
        self.play(Write(plane_surface),Write(plane_surface2))

        #show flux
        flux_tex = Tex("magnetischer Fluss").shift(UP*3).scale(1.5)
        func1 = lambda pos: RIGHT
        stream = StreamLines(func1, stroke_width=4, max_anchors_per_line=25, virtual_time=50, n_repeats=15,
                             x_range=[-5.7,2.3,7],y_range=[-4,2])

        self.play(Write(flux_tex))
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=5)
        self.wait(8)

        #equation
        forumla = MathTex(r"\phi _{B}=\int_{A}^{}\vec{B}\cdot d\vec{A}").shift(UP*3)

        self.play(FadeOut(flux_tex))
        self.play(Write(forumla))
        self.wait(7)
        self.play(stream.animate.set_opacity(0), fieldLines.animate.set_opacity(0.2))
        stream.end_animation()
        self.remove(stream)

        #different surfaces
        self.play(FadeOut(VGroup(plane_surface,plane_surface2)))
        self.move_camera(theta=-140*DEGREES, phi=60*DEGREES)
        self.begin_ambient_camera_rotation(0.09)

        circ = Circle(radius=2, color=BLUE, fill_opacity=0.5).rotate(PI/2, UP)
        self.play(Write(circ))
        self.wait(6)
        
        loop = Circle(radius=2,color=PURE_GREEN).rotate(PI/2,UP) 
        self.play(Write(loop))
        self.wait(6)

class LineIntegral(ThreeDScene):
    def construct(self):

        curve = MathTex(r"C",r":\vec{r}(t)=cos(t)",r"\hat{i}",r"+sin(t)",r"\hat{j}",r"+0",r"\hat{k}").to_corner(UL)
        curve[0].set_color(RED)
        curve[2].set_color(PURE_RED)
        curve[4].set_color(PURE_GREEN)
        curve[6].set_color(PURE_BLUE)
        b1 = SurroundingRectangle(curve[0:5],color=BLACK,fill_color=BLACK,fill_opacity=0.9, stroke_opacity=0).move_to(curve[0:5])
        interval = MathTex(r"t \in [0,2\pi]").to_corner(UR)

        def func(t):
            return (np.cos(t), np.sin(t), 0)
        def func2(t):
            return (np.cos(t), np.sin(t), np.sin(t)**2)
        def func3(u,v):
            return (np.cos(u), np.sin(u), v*np.sin(u)**2)

        axis = ThreeDAxes(x_range=[-2,2],y_range=[-2,2],z_range=[-2,2], z_length=4)
        circ = ParametricFunction(func, t_range = (0, 8*PI), fill_opacity=0).set_color(RED)

        #basics
        self.wait(frozen_frame=False)
        self.add_fixed_in_frame_mobjects(b1,curve)
        self.play(Write(VGroup(b1,curve)))
        self.wait(6)
        self.move_camera(frame_center=[-1,0,0], zoom=2)
        self.play(Write(axis))
        self.wait()
        self.play(Write(circ), run_time=6)
        self.wait(6)

        #hats and parameters
        ihat_tex = MathTex(r"\hat{i}").set_color(PURE_RED).move_to([1,-1,0])
        jhat_tex = MathTex(r"\hat{j}").set_color(PURE_GREEN).move_to([1,1,0])
        ihat = Vector([1,0]).set_color(PURE_RED)
        jhat = Vector([0,1]).set_color(PURE_GREEN)
        self.play(Write(VGroup(ihat_tex,jhat_tex)), GrowArrow(ihat), GrowArrow(jhat), run_time=2)
        self.wait(6)

        #boundaries
        self.add_fixed_in_frame_mobjects(interval)
        self.play(Write(interval))
        self.wait(6)
        self.move_camera(frame_center=[0,0,0], zoom=1,phi=60*DEGREES, theta=-45*DEGREES)
        self.wait()
        #show basis vector k
        khat = Vector([0,0,1]).set_color(PURE_BLUE).set_z_index(99)
        khat_tex = MathTex(r"\hat{k}").set_color(PURE_BLUE).move_to([-0.4,0,0.3]).rotate(PI/2,axis=RIGHT).rotate(PI/2,axis=OUT)

        self.play(FadeOut(curve[5:]), Unwrite(interval))
        self.wait()
        self.move_camera(zoom=4)
        self.wait()
        self.play(Write(khat_tex), GrowArrow(khat))
        self.wait(6)

        #paraboliod
        paraboloid = ParametricFunction(func2, t_range = (0, 8*PI), fill_opacity=0).set_color(WHITE)

        self.play(FadeOut(VGroup(ihat_tex,jhat_tex,khat,khat_tex, ihat, jhat)))
        self.wait(6)
        self.play(axis.animate.set_opacity(0.4))
        self.wait()
        self.move_camera(zoom=3, frame_center=[0,0,0.5])
        self.wait()
        self.play(Write(paraboloid), run_time=3)
        self.wait(2)

        #function
        functPara = MathTex(r"f(x,y)=y^{2}").next_to(curve,DOWN).to_edge(LEFT)
        self.add_fixed_in_frame_mobjects(functPara)
        self.play(Write(functPara))

        # surface and area
        surf = Surface(func3, u_range=[0, 2*PI], v_range=[0,1], resolution=[300,1], fill_opacity=1, fill_color=BLUE, checkerboard_colors=[BLUE_D, BLUE_D])
        area = MathTex(r"A",r"=?").to_edge(LEFT)
        area[0].set_color(BLUE)

        self.play(Create(surf), run_time=3)
        self.wait(17)
        self.add_fixed_in_frame_mobjects(area)
        self.play(Write(area))
        self.wait(4)
        #small rectangles
        surf2 = Surface(func3, u_range=[0, 2*PI], v_range=[0,1], resolution=[10,1], fill_opacity=1, should_make_jagged=True)
        self.play(ReplacementTransform(surf,surf2), run_time=2)
        self.wait(5)
        #f and ds
        dsCurve = ParametricFunction(func, t_range = (7*PI/5, 8*PI/5), fill_opacity=0).set_color(YELLOW)
        ds_tex = MathTex(r"ds").set_color(YELLOW).to_edge(DOWN).scale(1.41).shift(UP*0.6)
        fxyLine = Line3D(start=[-0.309,-1.2,0.17], end=[-0.313,-1.2,1.06]).set_color(RED)
        fxy_tex = MathTex(r"f(x,y)").set_color(RED).to_edge(LEFT).shift(DOWN+ RIGHT*2)

        self.play(FadeOut(VGroup(b1,curve[0:5],functPara,area)))
        self.move_camera(theta=-PI/2, frame_center=[0,0,0.2])
        self.play(circ.animate.set_color(GRAY_D))
        self.wait(5)

        self.play(DrawBorderThenFill(dsCurve))

        self.add_fixed_in_frame_mobjects(ds_tex)
        self.play(Write(ds_tex))
        self.wait(5)

        self.play(Write(fxyLine))
        self.wait()

        self.add_fixed_in_frame_mobjects(fxy_tex)
        self.play(Write(fxy_tex))
        self.wait(5)

        #integral
        line_int = MathTex(r"\int_{C}^{}",r"f(x,y)",r"ds").to_corner(UL)
        line_int[1].set_color(RED)
        line_int[2].set_color(YELLOW)

        self.add_fixed_in_frame_mobjects(line_int)
        self.play(Write(line_int))
        self.wait(7)

        #final ?
        surf3 = Surface(func3, u_range=[0, 2*PI], v_range=[0,1], resolution=[40,1], fill_opacity=1)
        surf4 = Surface(func3, u_range=[0, 2*PI], v_range=[0,1], resolution=[80,1], fill_opacity=1)
        surf5 = Surface(func3, u_range=[0, 2*PI], v_range=[0,1], resolution=[150,1], fill_opacity=1)
        surf6 = Surface(func3, u_range=[0, 2*PI], v_range=[0,1], resolution=[200,1], fill_opacity=1)
        self.play(FadeOut(dsCurve), FadeOut(fxyLine), ReplacementTransform(surf2,surf3))
        self.wait()
        self.play(ReplacementTransform(surf2,surf3))
        self.wait()
        self.play(ReplacementTransform(surf3,surf4))
        self.wait()
        self.play(ReplacementTransform(surf4,surf5))
        self.wait()
        self.play(ReplacementTransform(surf5,surf6))
        self.wait()

class FaradayLineIntegral(ThreeDScene):
    def construct(self):

        def vecField2(pos):
            r = 0.6
            b = 5
            e = 0.1
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = -b*y/(x**2 + y**2 + e) 
            field[1] = b*x/(x**2 + y**2 + e)
            if field[0]**2 + field[1]**2 < r:
                return 0*RIGHT + 0*UP
            else:
                return field[0]*RIGHT + field[1]*UP

        #loop
        loop = Circle(radius=2,color=PURE_GREEN, fill_color=PURE_BLUE, fill_opacity=0.4).rotate(PI/2,UP) 

        self.wait()
        self.play(DrawBorderThenFill(loop))
        self.move_camera(phi=90*DEGREES, theta=0*DEGREES, run_time=3)

        #line integral
        lineInt = MathTex(r"\oint_{\partial A}^{}\vec{E}\cdot d\vec{l}").to_corner(UL)
        lineInt[0][1].set_color(PURE_GREEN)
        lineInt[0][2].set_color(PURE_BLUE)
        b1 = SurroundingRectangle(lineInt,color=BLACK,fill_color=BLACK,fill_opacity=0.9, stroke_opacity=0).move_to(lineInt)
        self.add_fixed_in_frame_mobjects(b1,lineInt)
        self.play(Write(VGroup(b1,lineInt)))
        self.wait(12)

        #vec T
        time = ValueTracker(PI/2)
        rotate_time = 12
        t_vec = Vector([0,-1], color=RED).move_to([0,0,2]).rotate(PI/2, UP)
        t_tex = MathTex(r"\vec{T}").set_color(RED)
        t_tex.add_updater(lambda mob: mob.next_to(t_vec,OUT, buff=0.5))
        b2 = SurroundingRectangle(t_tex,color=BLACK,fill_color=BLACK,fill_opacity=0.9, stroke_opacity=0).move_to(t_tex)
        b2.add_updater(lambda mob: mob.move_to(t_tex,OUT))

        self.play(GrowArrow(t_vec))
        self.wait(frozen_frame=False)
        self.add_fixed_orientation_mobjects(b2,t_tex)
        self.play(Write(VGroup(b2,t_tex)))

        t_vec.add_updater(lambda mob, dt: mob.move_to([0, 2*np.cos(time.get_value()), 2*np.sin(time.get_value())]).rotate(2*PI*dt/rotate_time, RIGHT))
        t_vec.suspend_updating()
        self.wait(4,frozen_frame=False)
        t_vec.resume_updating()
        self.play(time.animate.set_value(2*PI+PI/2), rate_func=linear, run_time=rotate_time)

        #dl ds T
        dl_equation = MathTex(r"d \vec{l}",r"=",r"\vec{T}",r"ds").next_to(lineInt,DOWN).to_edge(LEFT)
        dl_equation[2].set_color(RED)
        dl_equation[3].set_color(YELLOW)
        b3 = SurroundingRectangle(dl_equation,color=BLACK,fill_color=BLACK,fill_opacity=0.9, stroke_opacity=0).move_to(dl_equation)

        t_vec.suspend_updating()

        self.wait(frozen_frame=False)
        self.add_fixed_in_frame_mobjects(b3,dl_equation)
        self.play(Write(VGroup(b3,dl_equation)))
        self.wait(5,frozen_frame=False)

        # efield
        colors1 = [BLUE, YELLOW, YELLOW, ORANGE, ORANGE, RED]
        vecField1Func1 = lambda pos: vecField2(pos=pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=3.2,min_color_scheme_value=0.8, colors=colors1, x_range=[-6,6], y_range=[-6,6]).rotate(PI/2, UP).set_z_index(-3)

        t_vec.resume_updating()
        self.play(time.animate.set_value(4*PI+PI/2), rate_func=linear, run_time=rotate_time)

        t_vec.suspend_updating()
        self.play(Create(vector_field1))
        self.wait(2)
        t_vec.resume_updating()

        self.play(time.animate.set_value(6*PI+PI/2), rate_func=linear, run_time=rotate_time)
        self.play(time.animate.set_value(8*PI+PI/2), rate_func=linear, run_time=rotate_time)
        self.play(Rotate(vector_field1, 1*PI), time.animate.set_value(10*PI+PI/2), rate_func=linear, run_time=rotate_time)
        self.wait()

class LenzsLaw(ThreeDScene):
    def construct(self):

        func1 = lambda pos: vecField1(pos=pos)
        def vecField1(pos):
            e = 0.001
            s = 0.2
            x = pos[0]
            y = pos[1]
            normal1 = x**2 + (y-s)**2 + e
            normal2 = x**2 + (y+s)**2 + e
            field = [0,0]
            field[0] = (y-s)/(normal1) - (y+s)/(normal2)
            field[1] = (-x)/(normal1) + (x)/(normal2)
            return field[0]*RIGHT + field[1]*UP

        def currentFlow(x, b=1, c=10):
            return np.abs((c * x) / ((x**2 + b**2)**2)) +0.1

        #setup
        north_pole = Prism(dimensions=[2,1,1], fill_color=BLUE, fill_opacity=1).move_to([1,0,0])
        south_pole = Prism(dimensions=[2,1,1], fill_color=RED, fill_opacity=1).move_to([-1,0,0])
        stream = SVGMobject("Magnetfield.svg", use_svg_cache=False).set_fill(opacity=0).scale(8).set_z_index(-1)
        center = stream.get_center() 
        paths = stream.family_members_with_points()
        distances = [np.linalg.norm(path.get_center() - center) for path in paths]
        max_distance = max(distances)
        for path, dist in zip(paths, distances):
            t = dist / max_distance  # 0 = center, 1 = farthest
            color = color_gradient([BLUE, RED, BLACK], 100)[int(t*99)]
            path.set_stroke(color=color, width=0.3)
        stream = VGroup(*paths).set_z_index(-1)
        magnet = VGroup(north_pole, south_pole, stream).set_z_index(1)

        loop = Circle(radius=2,color=GREEN).rotate(PI/2,UP) 
        integral_form = MathTex(r"\oint_{\partial A}^{}\vec{E}\cdot d\vec{l}=-\frac{d}{dt}\int_{A}^{}\vec{B}\cdot d\vec{A}").to_corner(UR)
        b1 = SurroundingRectangle(integral_form,color=BLACK,fill_color=BLACK,fill_opacity=0.9, stroke_opacity=0).move_to(integral_form)

        self.wait()
        self.play(FadeIn(magnet))
        self.move_camera(phi=60*DEGREES, theta=-45*DEGREES)
        self.play(Write(loop))
        
        self.play(magnet.animate.move_to([-4,0,0]), run_time=1.6)
        self.add_fixed_in_frame_mobjects(b1,integral_form)
        self.play(Write(integral_form), Write(b1))

        #move magnet
        vec1 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,0,2]).rotate(PI/2,OUT)
        vec2 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,2,0]).rotate(PI/2,UP)
        vec3 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,0,-2]).rotate(-PI/2,OUT)
        vec4 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,-2,0]).rotate(-PI/2,UP)
        l1 = Line(start=[0,0,2], end=[0,0,2], color=YELLOW)
        l2 = Line(start=[0,2,0], end=[0,2,0], color=YELLOW)
        l3 = Line(start=[0,0,-2], end=[0,0,-2], color=YELLOW)
        l4 = Line(start=[0,-2,0], end=[0,-2,0], color=YELLOW)
        vec1.add_updater(lambda mob: mob.set_y(currentFlow(magnet.get_x())))
        vec2.add_updater(lambda mob: mob.set_z(-currentFlow(magnet.get_x())))
        vec3.add_updater(lambda mob: mob.set_y(-currentFlow(magnet.get_x())))
        vec4.add_updater(lambda mob: mob.set_z(currentFlow(magnet.get_x())))
        l1.add_updater(lambda mob: mob.become(Line(start=[0,0,2], end=vec1.get_center(), color=YELLOW)))
        l2.add_updater(lambda mob: mob.become(Line(start=[0,2,0], end=vec2.get_center(), color=YELLOW)))
        l3.add_updater(lambda mob: mob.become(Line(start=[0,0,-2], end=vec3.get_center(), color=YELLOW)))
        l4.add_updater(lambda mob: mob.become(Line(start=[0,-2,0], end=vec4.get_center(), color=YELLOW)))
        vecs = VGroup(vec1,vec2,vec3,vec4, l1,l2,l3,l4)

        self.add(vecs)

        #show induced magnetic field
        stream2 = SVGMobject("Magnetfield.svg", use_svg_cache=False).set_fill(opacity=0).scale(6).set_z_index(-1)
        center = stream2.get_center() 
        paths = stream2.family_members_with_points()
        distances = [np.linalg.norm(path.get_center() - center) for path in paths]
        max_distance = max(distances)
        for path, dist in zip(paths, distances):
            t = dist / max_distance  # 0 = center, 1 = farthest
            color = color_gradient([BLUE, RED, BLACK], 100)[int(t*99)]
            path.set_stroke(color=color, width=1.1)
        stream2 = VGroup(*paths).set_z_index(-1).rotate(PI,OUT).rotate(PI/2,RIGHT)
        stream2.add_updater(lambda mob: mob.scale_to_fit_width(currentFlow(magnet.get_x(), b=1.3, c=100)))
        self.add(stream2)

        self.play(magnet.animate.move_to([4,0,0]), rate_func=linear, run_time=6)
        self.play(magnet.animate.move_to([-4,0,0]), rate_func=linear, run_time=6)
        self.play(magnet.animate.move_to([4,0,0]), rate_func=linear, run_time=6)
        self.play(magnet.animate.move_to([-4,0,0]), rate_func=linear, run_time=6)
        self.play(magnet.animate.move_to([4,0,0]), rate_func=linear, run_time=6)
        self.play(magnet.animate.move_to([-4,0,0]), rate_func=linear, run_time=6)

class AmpereIntro(ThreeDScene):
    def construct(self):

        def vecField1(pos):
            r = 0.03
            b = 1
            e = 0.01
            x = pos[0]
            y = pos[1]
            norm = x**2 + y**2 + e
            field = [0,0]
            field[0] = -b*y/norm
            field[1] = b*x/norm
            if field[0]**2 + field[1]**2 < r:
                return 0*RIGHT + 0*UP
            else:
                return field[0]*RIGHT + field[1]*UP


        #pipe
        pipe = Cylinder(radius=0.5, height=6, resolution=[1,20])
        pipe2 = Cylinder(radius=0.5, height=6, resolution=[1,10], v_range=[0,PI])

        self.move_camera(phi=60*DEGREES)
        self.begin_ambient_camera_rotation(0.1)

        self.wait()
        self.play(Create(pipe))
        self.play(ReplacementTransform(pipe,pipe2))

        #current
        func1 = lambda pos: RIGHT
        stream = StreamLines(func1, stroke_width=4, max_anchors_per_line=25, virtual_time=1, n_repeats=1,
                             y_range=[-0.2,0.2], x_range=[-2.2,2.2]).rotate(PI/2,OUT).rotate(PI/2,RIGHT).move_to(pipe2)
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=1)
        self.wait(1)

        # bfield
        colors1 = [BLUE, YELLOW, YELLOW, ORANGE, ORANGE, RED]
        vecField1Func1 = lambda pos: vecField1(pos=pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=0.8, min_color_scheme_value=0.2, colors=colors1, x_range=[-6,6], y_range=[-6,6])
        self.play(FadeIn(vector_field1))
        self.wait(4)

        #law
        equation = MathTex(r"\nabla \times ",r"\vec{B}",r"=\mu_{0}",r"\vec{J}").to_corner(UL)
        law_tex = Tex("Ampèresches Gesetz").to_corner(UR)

        self.add_fixed_in_frame_mobjects(law_tex)
        self.play(Write(law_tex))

        self.add_fixed_in_frame_mobjects(equation)
        self.play(Write(equation))

        self.wait(14)

class CurrentDensityVector(ThreeDScene):
    def construct(self):

        #setup
        surface = Circle(radius=3, color=BLUE, fill_opacity=0.5)

        self.wait()
        self.play(DrawBorderThenFill(surface))
        self.move_camera(phi=60*DEGREES)

        #current
        func1 = lambda pos: RIGHT
        stream = StreamLines(func1, stroke_width=4, max_anchors_per_line=25, virtual_time=1, n_repeats=1,
                             y_range=[-2,2], x_range=[-2.2,2.2], color=PURE_GREEN).rotate(PI/2,OUT).rotate(PI/2,RIGHT).move_to(surface)
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=1)
        self.wait(6)

        #intro J
        formula1 = MathTex(r"\vec{J}= \frac{dI}{d \vec{A}}").to_corner(UL)
        self.add_fixed_in_frame_mobjects(formula1)
        self.play(Write(formula1))
        self.wait(6)

        dsurface = Circle(radius=2, color=YELLOW, fill_opacity=0.5)
        dA = MathTex(r"dA").next_to(surface,RIGHT).set_color(YELLOW)

        self.play(DrawBorderThenFill(dsurface))
        self.add_fixed_orientation_mobjects(dA)
        self.play(Write(dA))
        self.wait(6)
        self.play(dsurface.animate.scale(0.1),run_time=2)

        #nomal
        normal_vec = Vector([0,1], color=RED).rotate(PI/2, RIGHT)

        self.play(GrowArrow(normal_vec))
        self.wait(4)

        #I correlation
        formula2 = MathTex(r"dI= \vec{J} \cdot d \vec{A}").to_corner(UL).shift(DOWN*2)
        formula3 = MathTex(r"I= \int \vec{J} \cdot d \vec{A}").to_corner(UL).shift(DOWN*4)

        self.add_fixed_in_frame_mobjects(formula2)
        self.play(FadeIn(formula2))
        self.add_fixed_in_frame_mobjects(formula3)
        self.play(FadeIn(formula3))
        self.wait(7)

class Mu0vsEpsilon0(Scene):
    def construct(self):
        
        eps0 = MathTex(r"\varepsilon_{0}").shift(LEFT*3+DOWN*3)
        mu0 = MathTex(r"\mu_{0}").shift(LEFT*-3+DOWN*3)

        core1 = Circle(radius=0.4,color=PURE_GREEN,fill_color=PURE_GREEN,fill_opacity=1)
        corss3 = Rectangle(height=0.03,width=0.3,fill_opacity=1)
        electron = VGroup(core1,corss3).shift(LEFT*3).scale(0.7)
        func1 = lambda pos: 3*(pos[0]/(pos[0]**2 + pos[1]**2 +0.0001)) * RIGHT + 3*(pos[1]/(pos[0]**2 + pos[1]**2 +0.0001)) * UP
        vector_field = ArrowVectorField(func1,x_range=[-2,2],y_range=[-2,2], color=BLUE).move_to(electron).scale(1)

        def vecField1(pos):
            e = 0.0001
            s = 0.1
            x = pos[0]
            y = pos[1]
            normal1 = x**2 + (y-s)**2 + e
            normal2 = x**2 + (y+s)**2 + e
            field = [0,0]
            field[0] = (y-s)/(normal1) - (y+s)/(normal2)
            field[1] = (-x)/(normal1) + (x)/(normal2)
            return 15*field[0]*RIGHT + 15*field[1]*UP
        
        north_pole = Rectangle(width=1,height=0.5,color=BLUE,fill_opacity=1).shift(LEFT*0.5)
        south_pole = Rectangle(width=1,height=0.5,color=RED,fill_opacity=1).shift(LEFT*-0.5)
        north_pole_tex = MathTex(r"N").move_to(north_pole)
        south_pole_tex = MathTex(r"S").move_to(south_pole)
        magnet = VGroup(north_pole,south_pole,north_pole_tex,south_pole_tex).move_to([0,0,0.1]).set_z_index(1).shift(RIGHT*3)

        func2 = lambda pos: vecField1(pos=pos)
        vector_field2 = ArrowVectorField(func=func2,color=BLUE,x_range=[-2,2,0.5],y_range=[-2,2,0.5]).move_to(magnet)


        #comparion vacuum
        self.wait()
        self.play(Write(electron))
        self.play(Create(vector_field))
        self.play(Write(eps0))

        self.wait(5)
        self.play(Write(magnet))
        self.play(Create(vector_field2))
        self.play(Write(mu0))
        self.wait(8)

        #new comparisons
        self.play(FadeOut(VGroup(electron,magnet,vector_field,vector_field2)))

        elctrism = Tex(r"Elektrizität:").shift(LEFT*3+UP*3)
        magnetism = Tex(r"Magnetismus:").shift(LEFT*-3+UP*3)
        chargedensisty = MathTex(r"\rho").shift(LEFT*3+UP*1)
        currentdensisty = MathTex(r"\vec{J}").shift(LEFT*-3+UP*1)
        eTo = MathTex(r"e\rightarrow").shift(LEFT*3+UP*-1)
        eField = Tex("E-Feld").next_to(eTo,RIGHT)
        iTo = MathTex(r"I\rightarrow").shift(LEFT*-3+UP*-1)
        bField = Tex("B-Feld").next_to(iTo,RIGHT)

        self.wait()
        self.play(Write(elctrism))
        self.wait()
        self.play(Write(magnetism))
        self.wait()
        self.play(Write(chargedensisty))
        self.wait()
        self.play(Write(currentdensisty))
        self.wait(3)
        self.play(Write(eTo))
        self.wait()
        self.play(Write(eField))
        self.wait()
        self.play(Write(iTo))
        self.wait()
        self.play(Write(bField))
        self.wait()

class AmpereDiffRecap(ThreeDScene):
    def construct(self):

        def vecField1(pos):
            r = 0.03
            b = 1
            e = 0.01
            x = pos[0]
            y = pos[1]
            norm = x**2 + y**2 + e
            field = [0,0]
            field[0] = -b*y/norm
            field[1] = b*x/norm
            if field[0]**2 + field[1]**2 < r:
                return 0*RIGHT + 0*UP
            else:
                return field[0]*RIGHT + field[1]*UP


        #pipe
        pipe = Cylinder(radius=0.5, height=6, resolution=[1,20])
        pipe2 = Cylinder(radius=0.5, height=6, resolution=[1,10], v_range=[0,PI])

        self.move_camera(phi=60*DEGREES)
        self.begin_ambient_camera_rotation(0.1)

        self.wait()
        self.play(Create(pipe))
        self.play(ReplacementTransform(pipe,pipe2))

        #law
        equation = MathTex(r"\nabla \times ",r"\vec{B}",r"=\mu_{0}",r"\vec{J}").to_corner(UL)

        self.add_fixed_in_frame_mobjects(equation)
        self.play(Write(equation))

        #current
        func1 = lambda pos: RIGHT
        stream = StreamLines(func1, stroke_width=4, max_anchors_per_line=25, virtual_time=1, n_repeats=1,
                             y_range=[-0.2,0.2], x_range=[-2.2,2.2]).rotate(PI/2,OUT).rotate(PI/2,RIGHT).move_to(pipe2)
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=1)
        self.wait(1)

        # efield
        colors1 = [BLUE, YELLOW, YELLOW, ORANGE, ORANGE, RED]
        vecField1Func1 = lambda pos: vecField1(pos=pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=0.8, min_color_scheme_value=0.2, colors=colors1, x_range=[-6,6], y_range=[-6,6])
        self.play(FadeIn(vector_field1))
        self.wait(20)

class AmpereCapacitor(ThreeDScene):
    def construct(self):

        def vecField1(pos):
            r = 0.03
            b = 1
            e = 0.01
            x = pos[0]
            y = pos[1]
            norm = x**2 + y**2 + e
            field = [0,0]
            field[0] = -b*y/norm
            field[1] = b*x/norm
            if field[0]**2 + field[1]**2 < r:
                return 0*RIGHT + 0*UP
            else:
                return field[0]*RIGHT + field[1]*UP


        #pipe
        plate1 = Prism([2,2,0.2], fill_color=WHITE).move_to([0,0,-1])
        plate2 = Prism([2,2,0.2], fill_color=WHITE).move_to([0,0,1])

        pipe = Cylinder(radius=0.5, height=6, resolution=[1,20]).next_to(plate1, IN, buff=0)
        pipe2 = Cylinder(radius=0.5, height=6, resolution=[1,20]).next_to(plate2, OUT, buff=0)


        self.move_camera(phi=60*DEGREES)
        self.begin_ambient_camera_rotation(0.1)

        self.wait()
        self.play(Create(pipe))
        self.play(Create(plate1))
        self.play(Create(plate2))
        self.play(Create(pipe2))
        self.wait(6)

        #law
        equation = MathTex(r"\nabla \times ",r"\vec{B}",r"=\mu_{0}",r"\vec{J}").to_corner(UL)

        self.add_fixed_in_frame_mobjects(equation)
        self.play(Write(equation))
        self.wait(3)

        # bfield
        colors1 = [BLUE, YELLOW, YELLOW, ORANGE, ORANGE, RED]
        vecField1Func1 = lambda pos: vecField1(pos=pos)
        vecField1Func2 = lambda pos: vecField1(pos=-pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=0.8, min_color_scheme_value=0.2, colors=colors1, x_range=[-6,6], y_range=[-6,6])
        vector_field2 = ArrowVectorField(vecField1Func2, max_color_scheme_value=0.8, min_color_scheme_value=0.2, colors=colors1, x_range=[-6,6], y_range=[-6,6])
        
        #charge discharge
        self.play(plate1.animate.set_fill_color(GREEN),plate2.animate.set_fill_color(RED),FadeIn(vector_field1), rate_func=linear, run_time=3)
        self.remove(vector_field1)
        self.add(vector_field2)
        self.play(plate1.animate.set_fill_color(WHITE),plate2.animate.set_fill_color(WHITE),FadeOut(vector_field2), rate_func=linear, run_time=5)

        self.play(plate1.animate.set_fill_color(GREEN),plate2.animate.set_fill_color(RED),FadeIn(vector_field1), rate_func=linear, run_time=3)
        self.remove(vector_field1)
        self.add(vector_field2)
        self.play(plate1.animate.set_fill_color(WHITE),plate2.animate.set_fill_color(WHITE),FadeOut(vector_field2), rate_func=linear, run_time=5)

        self.play(plate1.animate.set_fill_color(GREEN),plate2.animate.set_fill_color(RED),FadeIn(vector_field1), rate_func=linear, run_time=3)
        self.remove(vector_field1)
        self.add(vector_field2)
        self.play(plate1.animate.set_fill_color(WHITE),plate2.animate.set_fill_color(WHITE),FadeOut(vector_field2), rate_func=linear, run_time=5)

        self.play(plate1.animate.set_fill_color(GREEN),plate2.animate.set_fill_color(RED),FadeIn(vector_field1), rate_func=linear, run_time=3)
        self.remove(vector_field1)
        self.add(vector_field2)
        self.play(plate1.animate.set_fill_color(WHITE),plate2.animate.set_fill_color(WHITE),FadeOut(vector_field2), rate_func=linear, run_time=5)

        #newlaw
        equation2 = MathTex(r"\nabla \times ",r"\vec{B}",r"=\mu_{0}",r"\vec{J} + \mu_{0} \varepsilon_{0} \frac{\partial \vec{E}}{\partial t}").to_corner(UL)

        self.add_fixed_in_frame_mobjects(equation2)
        self.play(FadeOut(equation), FadeIn(equation2))

        #charge discharge
        self.play(plate1.animate.set_fill_color(GREEN),plate2.animate.set_fill_color(RED),FadeIn(vector_field1), rate_func=linear, run_time=3)
        self.remove(vector_field1)
        self.add(vector_field2)
        self.play(plate1.animate.set_fill_color(WHITE),plate2.animate.set_fill_color(WHITE),FadeOut(vector_field2), rate_func=linear, run_time=3)

        self.play(plate1.animate.set_fill_color(GREEN),plate2.animate.set_fill_color(RED),FadeIn(vector_field1), rate_func=linear, run_time=3)
        self.remove(vector_field1)
        self.add(vector_field2)
        self.play(plate1.animate.set_fill_color(WHITE),plate2.animate.set_fill_color(WHITE),FadeOut(vector_field2), rate_func=linear, run_time=3)

        self.play(plate1.animate.set_fill_color(GREEN),plate2.animate.set_fill_color(RED),FadeIn(vector_field1), rate_func=linear, run_time=3)
        self.remove(vector_field1)
        self.add(vector_field2)
        self.play(plate1.animate.set_fill_color(WHITE),plate2.animate.set_fill_color(WHITE),FadeOut(vector_field2), rate_func=linear, run_time=3)

        self.play(plate1.animate.set_fill_color(GREEN),plate2.animate.set_fill_color(RED),FadeIn(vector_field1), rate_func=linear, run_time=3)
        self.remove(vector_field1)
        self.add(vector_field2)
        self.play(plate1.animate.set_fill_color(WHITE),plate2.animate.set_fill_color(WHITE),FadeOut(vector_field2), rate_func=linear, run_time=3)

class AmpereIntegralForm(ThreeDScene):
    def construct(self):

        def vector_field(pos,q=1):
            x, y, _ = pos
            return np.array([
                np.sin(q*(x+4.3)+q*(y+12.8)),
                np.cos(q*(x+4.3)-q*(y+12.8)),
                0
            ])
        
        dt = 4
        def flow_function(p):
            return p + dt * vector_field(8*p,0.18)

        def vecField1(pos):
            r = 0.03
            b = 1
            e = 0.01
            x = pos[0]
            y = pos[1]
            norm = x**2 + y**2 + e
            field = [0,0]
            field[0] = -b*y/norm
            field[1] = b*x/norm
            if field[0]**2 + field[1]**2 < r:
                return 0*RIGHT + 0*UP
            else:
                return field[0]*RIGHT + field[1]*UP

        square = Circle(color=BLUE, radius=1).set_z_index(-1)
        square.set_fill(BLUE, opacity=0.4)

        #pipe
        pipe = Cylinder(radius=0.25, height=6, resolution=[1,20], checkerboard_colors=[GREEN_D, GREEN_E], fill_color=GREEN)

        self.move_camera(phi=60*DEGREES)
        self.begin_ambient_camera_rotation(0.1)

        self.wait()
        self.play(Create(pipe))

        #current
        func1 = lambda pos: RIGHT
        stream = StreamLines(func1, stroke_width=4, max_anchors_per_line=25, virtual_time=1, n_repeats=1,
                             y_range=[-0.1,0.1], x_range=[-2.2,2.2]).rotate(PI/2,OUT).rotate(PI/2,RIGHT).move_to(pipe)
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=1)
        self.wait()

        #init
        colors1 = [BLUE, YELLOW, YELLOW, ORANGE, ORANGE, RED]
        vecField1Func1 = lambda pos: vecField1(pos=pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=0.8, min_color_scheme_value=0.2, colors=colors1, x_range=[-6,6], y_range=[-6,6])

        self.play(Write(square))
        self.wait(8)
        self.play(FadeIn(vector_field1))
        self.wait(3)

        #field stretch
        self.play(
            square.animate.apply_function(flow_function),
            run_time=15,
            rate_func=linear
        )

        #formula
        formula = MathTex(r"\oint_{\partial A}^{}\vec{B}\cdot d\vec{l}",r"=\mu_{0} I_{ein} + \mu_{0} \varepsilon_{0} \frac{d \phi_{E}}{dt}").scale(0.9).to_corner(UL)

        self.add_fixed_in_frame_mobjects(formula[0])
        self.play(Write(formula[0]))
        self.wait(13)
        self.add_fixed_in_frame_mobjects(formula[1])
        self.play(Write(formula[1]))
        self.wait(13)

class AmpereSymbolSheet(Scene):
    def construct(self):

        formula = MathTex(r"\oint_{\partial A}^{}\vec{B}\cdot d\vec{l}",r"=\mu_{0} I_{ein} + \mu_{0} \varepsilon_{0} \frac{d \phi_{E}}{dt}").scale(1).to_corner(UL)

        integral = MathTex(r"\oint=").to_corner(UL).shift(DOWN*3)
        partial = MathTex(r"\partial=").to_corner(UL).shift(DOWN*6)
        lineelement = MathTex(r"d\vec{l}=").to_corner(UR).shift(DOWN*0+LEFT*5)
        deriv = MathTex(r"\frac{d}{dt}=").to_corner(UR).shift(DOWN*3+LEFT*5)
        flux = MathTex(r"\phi_{E}=").to_corner(UR).shift(DOWN*6+LEFT*5)

        integral_tex = Tex("geschlossenes Integral").next_to(integral,RIGHT)
        partial_tex = Tex("Rand von").next_to(partial,RIGHT)
        lineelement_tex = Tex("Linienelement").next_to(lineelement,RIGHT)
        deirv_tex = Tex("Ableitung nach Zeit").next_to(deriv,RIGHT)
        flux_tex = Tex("elektrischer Fluss").next_to(flux,RIGHT)

        self.add(formula)
        self.add(integral,partial,lineelement,deriv,flux)
        self.add(integral_tex,partial_tex,lineelement_tex,deirv_tex,flux_tex)

class GausSymbolSheet(Scene):
    def construct(self):

        formula = MathTex(r" \oint_{\partial V} \vec{B} \cdot d \vec{A} = 0").scale(1).to_corner(UL)

        integral = MathTex(r"\oint=").to_corner(UL).shift(DOWN*3)
        partial = MathTex(r"\partial=").to_corner(UL).shift(DOWN*6)
        lineelement = MathTex(r"d\vec{A}=").to_corner(UR).shift(DOWN*0+LEFT*5)
        deriv = MathTex(r"\vec{B}=").to_corner(UR).shift(DOWN*3+LEFT*5)

        integral_tex = Tex("geschlossenes Integral").next_to(integral,RIGHT)
        partial_tex = Tex("Rand von").next_to(partial,RIGHT)
        lineelement_tex = Tex("Oberflächenelement").next_to(lineelement,RIGHT)
        deirv_tex = Tex("magnetisches Feld").next_to(deriv,RIGHT)

        self.add(formula)
        self.add(integral,partial,lineelement,deriv)
        self.add(integral_tex,partial_tex,lineelement_tex,deirv_tex)

class OverviewEnd(ThreeDScene):
    def construct(self):   

        header = Tex("Maxwell-Gleichungen")
        maxwell = ImageMobject("maxwell.jpg")
        first = Tex("1.").shift(UP*2.3).to_edge(LEFT)
        second = Tex("2.").shift(UP*1).to_edge(LEFT)
        third = Tex("3.").shift(UP*-1).to_edge(LEFT)
        forth = Tex("4.").shift(UP*-3).to_edge(LEFT)

        equation1 = MathTex(r" \nabla \cdot \vec{E} = \frac{\rho }{\varepsilon _{0}}").shift(UP*2.3).next_to(first,RIGHT)
        equation2 = MathTex(r" \nabla \cdot \vec{B} = 0").shift(UP*1).next_to(second,RIGHT)
        equation3 = MathTex(r" \nabla \times \vec{E}=-\frac{\partial \vec{B}}{\partial t}").shift(UP*-1).next_to(third,RIGHT)
        equation4 = MathTex(r" \nabla \times \vec{B}=\mu_{0}(\vec{J}+\varepsilon _{0}\frac{\partial \vec{E}}{\partial t})").shift(UP*-3).next_to(forth,RIGHT)

        #overview
        self.add_sound("OverviewEnd.wav", time_offset=1)
        self.wait()
        self.add_fixed_in_frame_mobjects(header)
        self.play(FadeIn(header))
        self.play(header.animate.to_edge(UP))

        self.add_fixed_in_frame_mobjects(first,equation1)
        self.play(FadeIn(VGroup(first,equation1)))
        self.add_fixed_in_frame_mobjects(second,equation2)
        self.play(FadeIn(VGroup(second,equation2)))
        self.add_fixed_in_frame_mobjects(third,equation3)
        self.play(FadeIn(VGroup(third,equation3)))
        self.add_fixed_in_frame_mobjects(forth,equation4)
        self.play(FadeIn(VGroup(forth,equation4)))

        #short look at 3
        # setup view
        # 
        func1 = lambda pos: vecField1(pos=pos)
        def vecField1(pos):
            e = 0.001
            s = 0.2
            x = pos[0]
            y = pos[1]
            normal1 = x**2 + (y-s)**2 + e
            normal2 = x**2 + (y+s)**2 + e
            field = [0,0]
            field[0] = (y-s)/(normal1) - (y+s)/(normal2)
            field[1] = (-x)/(normal1) + (x)/(normal2)
            return field[0]*RIGHT + field[1]*UP

        def currentFlow(x, b=1, c=10):
            return (c * x) / ((x**2 + b**2)**2)

        #setup
        stream = SVGMobject("Magnetfield.svg", use_svg_cache=False).set_fill(opacity=0).scale(8).set_z_index(-1)
        center = stream.get_center() 
        paths = stream.family_members_with_points()
        distances = [np.linalg.norm(path.get_center() - center) for path in paths]
        max_distance = max(distances)
        for path, dist in zip(paths, distances):
            t = dist / max_distance  # 0 = center, 1 = farthest
            color = color_gradient([BLUE, RED, BLACK], 100)[int(t*99)]
            path.set_stroke(color=color, width=0.6)
        stream = VGroup(*paths).set_z_index(-1)
        north_pole = Prism(dimensions=[2,1,1], fill_color=BLUE, fill_opacity=1).move_to([1,0,0])
        south_pole = Prism(dimensions=[2,1,1], fill_color=RED, fill_opacity=1).move_to([-1,0,0])
        magnet = VGroup(north_pole, south_pole, stream).set_z_index(1)

        loop = Circle(radius=2,color=GREEN).rotate(PI/2,UP) 

        #move magnet
        vec1 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,0,2]).rotate(PI/2,OUT)
        vec2 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,2,0]).rotate(PI/2,UP)
        vec3 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,0,-2]).rotate(-PI/2,OUT)
        vec4 = Cube(side_length=0.15, fill_color=YELLOW, fill_opacity=1).move_to([0,-2,0]).rotate(-PI/2,UP)
        l1 = Line(start=[0,0,2], end=[0,0,2], color=YELLOW)
        l2 = Line(start=[0,2,0], end=[0,2,0], color=YELLOW)
        l3 = Line(start=[0,0,-2], end=[0,0,-2], color=YELLOW)
        l4 = Line(start=[0,-2,0], end=[0,-2,0], color=YELLOW)
        vec1.add_updater(lambda mob: mob.set_y(currentFlow(magnet.get_x())))
        vec2.add_updater(lambda mob: mob.set_z(-currentFlow(magnet.get_x())))
        vec3.add_updater(lambda mob: mob.set_y(-currentFlow(magnet.get_x())))
        vec4.add_updater(lambda mob: mob.set_z(currentFlow(magnet.get_x())))
        l1.add_updater(lambda mob: mob.become(Line(start=[0,0,2], end=vec1.get_center(), color=YELLOW)))
        l2.add_updater(lambda mob: mob.become(Line(start=[0,2,0], end=vec2.get_center(), color=YELLOW)))
        l3.add_updater(lambda mob: mob.become(Line(start=[0,0,-2], end=vec3.get_center(), color=YELLOW)))
        l4.add_updater(lambda mob: mob.become(Line(start=[0,-2,0], end=vec4.get_center(), color=YELLOW)))
        vecs = VGroup(vec1,vec2,vec3,vec4, l1,l2,l3,l4)
        # 
        # setup view
        # 


        self.play(VGroup(second,first,forth,equation2,equation1,equation4).animate.set_opacity(0.4), VGroup(third,equation3).animate.scale(1.2).to_edge(LEFT))

        self.move_camera(phi=60*DEGREES, theta=-45*DEGREES,frame_center=[-3,-3,-0.2], zoom=0.8)
        magnet.move_to([-4,0,0])
        self.play(FadeIn(magnet))
        self.play(Write(loop))

        #magnet
        self.add(vecs)
        self.play(magnet.animate.move_to([4,0,0]), rate_func=linear, run_time=6)

        #reset
        self.play(FadeOut(VGroup(magnet,loop,vecs)))

        # short look at 2
        self.play(VGroup(third,equation3).animate.set_opacity(0.4).scale(1/1.2).to_edge(LEFT), VGroup(forth,equation4).animate.scale(1.2).to_edge(LEFT).set_opacity(1))
        

        def vecField1(pos):
            r = 0.03
            b = 1
            e = 0.01
            x = pos[0]
            y = pos[1]
            norm = x**2 + y**2 + e
            field = [0,0]
            field[0] = -b*y/norm
            field[1] = b*x/norm
            if field[0]**2 + field[1]**2 < r:
                return 0*RIGHT + 0*UP
            else:
                return field[0]*RIGHT + field[1]*UP


        #pipe
        pipe2 = Cylinder(radius=0.5, height=6, resolution=[1,10], v_range=[0,PI])

        self.move_camera(phi=45*DEGREES, frame_center=[-3,-4,-0.2])

        self.play(Create(pipe2))

        # #current
        # func1 = lambda pos: RIGHT
        # stream = StreamLines(func1, stroke_width=4, max_anchors_per_line=25, virtual_time=1, n_repeats=1,
        #                      y_range=[-0.2,0.2], x_range=[-2.2,2.2]).rotate(PI/2,OUT).rotate(PI/2,RIGHT).move_to([0,-4,0])
        # self.add(stream)
        # stream.start_animation(warm_up=True, flow_speed=1)
        # self.wait(1)

        # bfield
        colors1 = [BLUE, YELLOW, YELLOW, ORANGE, ORANGE, RED]
        vecField1Func1 = lambda pos: vecField1(pos=pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=0.8, min_color_scheme_value=0.2, colors=colors1, x_range=[-6,6], y_range=[-6,6])
        self.play(FadeIn(vector_field1))
        self.wait(2)

class Ending(Scene):
    def construct(self):

        self.add_sound(sound_file="Ending.wav",time_offset=0)

        banner = ManimBanner().scale(0.5)
        bannertxt = Tex("https://www.manim.community/")
        musicimg = ImageMobject("3b1bmusiclogo.jpg").scale(0.8).set_z_index(-1)
        musicimgtxt = Tex("https://vincerubinetti.bandcamp.com/album/the-music-of-3blue1brown").scale(0.85)
        
        page1 = VGroup(banner,bannertxt,musicimgtxt)

        download = Tex("Download zum Vortrag, Skript, Code:").set_z_index(1)
        download2 = Tex("https://github.com/Namitera/Physik-Maxwell-Gleichungen-23.01.2026").scale(0.85).shift(DOWN).set_z_index(1)
        link1 = Tex("https://www.youtube.com/watch?v=rB83DpBJQsE")
        link2 = Text("https://www.youtube.com/watch?v=AIxiYG-gZ00").scale(0.7)
        link3 = Text("&list=PLHXZ9OQGMqxfW0GMqeUE1bLKaYor6kbHa").scale(0.7)
        link4 = Tex("https://www.youtube.com/watch?v=Yn-MEMaiA0Y")
        link5 = Tex("https://www.youtube.com/watch?v=nGQbA2jwkWI")
        link6 = Tex("https://www.youtube.com/watch?v=d8AIoU8vtzo")
        link7 = Tex("https://www.youtube.com/watch?v=F3QHUvr8d8I")
        link8 = Text("https://www.youtube.com/watch?v=QwUq8xM_8bY").scale(0.7)
        link9 = Tex("https://www.youtube.com/watch?v=q1eor6oIuUo")
        link10 = Tex("https://www.youtube.com/watch?v=hJD8ywGrXks")
        links = VGroup(link1,link2,link3,link4,link5,link6,link7,link8,link9,link10).arrange_in_grid(10,1,cell_alignment=LEFT, buff=1).shift(DOWN*9).set_z_index(-1)
        links.to_edge(LEFT)

        self.wait()
        self.play(banner.create())
        self.play(banner.expand())
        self.play(banner.animate.to_corner(UL))
        self.play(FadeIn(bannertxt))
        self.play(bannertxt.animate.next_to(banner,DOWN).align_to(banner,LEFT))
        self.wait(3)
        self.play(FadeIn(musicimg))
        self.play(musicimg.animate.to_edge(LEFT).shift(DOWN+LEFT*0.5))
        self.play(FadeIn(musicimgtxt))
        self.play(musicimgtxt.animate.next_to(musicimg,DOWN).align_to(musicimg,LEFT).shift(RIGHT*0.5+UP*0.3))
        self.wait(5)
        self.play(FadeOut(page1),FadeOut(musicimg))
        self.wait()

        #page2
        rec = Rectangle(color=WHITE, fill_color=BLACK, fill_opacity=1, width=20, height=5).shift(DOWN*4)
        page2 = VGroup(download,download2,rec)

        self.play(FadeIn(download))
        self.play(download.animate.to_corner(UL).shift(DOWN*5.5+LEFT*-0))
        self.play(FadeIn(download2))
        self.play(download2.animate.to_corner(UL).shift(DOWN*6.5+LEFT*-0))
        self.play(FadeIn(rec))
        self.add(links)
        self.play(links.animate.shift(UP*20), rate_func=linear, run_time=20)

        self.wait(1)
        self.play(FadeOut(page2))

class Zusammenfassung(Scene):
    def construct(self):

        first = Tex("1.").shift(UP*2.3).to_edge(LEFT)
        second = Tex("2.").shift(UP*1).to_edge(LEFT)
        third = Tex("3.").shift(UP*-1).to_edge(LEFT)
        forth = Tex("4.").shift(UP*-3).to_edge(LEFT)

        equation1 = MathTex(r" \nabla \cdot \vec{E} = \frac{\rho }{\varepsilon _{0}}").shift(UP*2.3).next_to(first,RIGHT)
        equation2 = MathTex(r" \nabla \cdot \vec{B} = 0").shift(UP*1).next_to(second,RIGHT)
        equation3 = MathTex(r" \nabla \times \vec{E}=-\frac{\partial \vec{B}}{\partial t}").shift(UP*-1).next_to(third,RIGHT)
        equation4 = MathTex(r" \nabla \times \vec{B}=\mu_{0}(\vec{J}+\varepsilon _{0}\frac{\partial \vec{E}}{\partial t})").shift(UP*-3).next_to(forth,RIGHT)

        equation5 = MathTex(r"\oint_{A}\vec{E}\cdot d\vec{A}=\frac{q}{\varepsilon_{0}}").shift(UP*2.3).to_edge(RIGHT)
        equation6 = MathTex(r" \oint_{\partial V} \vec{B} \cdot d \vec{A} = 0").shift(UP*1).to_edge(RIGHT)
        equation7 = MathTex(r"\oint_{\partial A}^{}\vec{E}\cdot d\vec{l}=-\frac{d}{dt}\int_{A}^{}\vec{B}\cdot d\vec{A}").shift(UP*-1).to_edge(RIGHT)
        equation8 = MathTex(r"\oint_{\partial A}^{}\vec{B}\cdot d\vec{l}",r"=\mu_{0} I_{ein} + \mu_{0} \varepsilon_{0} \frac{d \phi_{E}}{dt}").shift(UP*-3).to_edge(RIGHT)

        dif_tex = Tex("Differentielle Form:").shift(UP*3.5).to_edge(LEFT)
        int_tex = Tex("Integrale Form:").shift(UP*3.5).to_edge(RIGHT)

        self.add(first,second,third,forth,equation1,equation2,equation3,equation4,equation5,equation6,equation7,equation8,dif_tex,int_tex)

class ImgTest(ThreeDScene):
    def construct(self):

        s1 = FullScreenRectangle(color=PURE_RED)
        s2 = FullScreenRectangle(color=PURE_GREEN).scale(0.99)
        s3 = FullScreenRectangle(color=PURE_RED).scale(0.98)
        s4 = FullScreenRectangle(color=PURE_GREEN).scale(0.97)
        s5 = FullScreenRectangle(color=PURE_RED).scale(0.96)
        s6 = FullScreenRectangle(color=PURE_GREEN).scale(0.95)

        j = 0
        h = 1
        iu = "atojmahcuyia"
        for i in iu:
            u = Tex(f"{i}")
            j += 0.3
            h -= 0.06
            self.add(u.scale(h).shift(RIGHT*j))

        for i in range(1,41):
            l = Line(start=[0,0,0],end=[0,0.01*i,0]).shift(RIGHT*0.1*i+UP)
            self.add(l)

        for i in range(1,27):
            r = Square(color=BLUE).set_opacity(np.floor(i)/80).shift(LEFT*4+DOWN*3+ UP*0.2*i)
            self.add(r)

        for i in range(1,27):
            r = Square(color=WHITE).set_opacity(np.floor(i)/80).shift(LEFT*2.1+DOWN*3+ UP*0.2*i)
            self.add(r)

        r2 = Square(color=PURE_BLUE).shift(LEFT*5)
        r3 = Square(color=BLUE).shift(LEFT*5+UP)
        t2 = MathTex(r"0_{0}").shift(UP*2)
        t1 = Tex("Tex").shift(DOWN*2)
        #aiyu cham jota
        #atoj mahc uyia

        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=12,
            y_length=6,
        ).shift(UP*0.7)
        def f(x):
            return 0.25*x**3 - 1.3*x**2 + 1.4*x + 1.1
        graph = axes.plot(f, x_range=[0, 5], color=BLUE)
        finer_rects = axes.get_riemann_rectangles(
            graph,
            x_range=[4, 5],
            dx=0.01,
            input_sample_type="left",
            fill_opacity=1,
        ).to_corner(DR)

        sph = Sphere().move_to([3,3,0])

        self.add_fixed_in_frame_mobjects(finer_rects,sph)
        self.add_fixed_in_frame_mobjects(s1,s2,s3,s4,s5,s6,t1,t2,r2,r3)