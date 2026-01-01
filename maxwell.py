from manim import *


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
        equation4 = MathTex(r" \nabla \times \vec{B}=\mu_{0}(\vec{j}+\epsilon _{0}\frac{\partial \vec{E}}{\partial t})").shift(UP*-3).next_to(forth,RIGHT)

        #overview
        self.play(Write(header))
        self.play(header.animate.to_edge(UP))
        self.play(FadeIn(maxwell))
        self.play(maxwell.animate.shift(RIGHT*4))
        self.play(FadeIn(VGroup(first,equation1)))
        self.play(FadeIn(VGroup(second,equation2)))
        self.play(FadeIn(VGroup(third,equation3)))
        self.play(FadeIn(VGroup(forth,equation4)))

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
        self.play(FadeOut(VGroup(proton,vector_field)))

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
        
        stream = StreamLines(func1, stroke_width=2, max_anchors_per_line=300, virtual_time=50, n_repeats=1).set_z_index(-1)

        north_pole = Rectangle(width=1,height=0.5,color=BLUE,fill_opacity=1).shift(LEFT*0.5)
        south_pole = Rectangle(width=1,height=0.5,color=RED,fill_opacity=1).shift(LEFT*-0.5)
        north_pole_tex = MathTex(r"N").move_to(north_pole)
        south_pole_tex = MathTex(r"S").move_to(south_pole)
        magnet = VGroup(north_pole,south_pole,north_pole_tex,south_pole_tex).move_to([0,0,0.1]).set_z_index(1)

        #magnet and fieldlines
        self.play(Write(magnet))
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=3)
        self.wait(3)
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
        self.play(ReplacementTransform(magnet,magnet2), ReplacementTransform(magnet.copy(),magnet3))
        self.wait()

        #keine monos
        mono = Tex("keine magnetischen Monopole").shift(UP*3)
        exept = Tex("*soweit wir wissen").shift(UP*2).scale(0.9).align_to(mono,LEFT)

        self.play(Write(mono))
        self.play(FadeIn(exept))
        self.play(FadeOut(exept))
        self.play(FadeOut(magnet3), magnet2.animate.move_to([0,0,0.1]))

        stream2 = StreamLines(func1, stroke_width=2, max_anchors_per_line=300, virtual_time=50, n_repeats=1).set_z_index(-1)
        self.play(FadeIn(stream2))

        vector_field = ArrowVectorField(func=func1,max_color_scheme_value=0.1,min_color_scheme_value=0.01)
        self.play(FadeIn(vector_field), FadeOut(stream2))

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
        self.play(Write(p1))
        self.play(Write(np))

        #schreibweisen
        self.play(Write(p1tex))
        self.play(Write(p1tex2))

        #switch to basis vectors
        self.play(Unwrite(p1tex),Unwrite(p1tex2), Unwrite(np))

        self.play(x.animate.set_color(RED))
        self.play(ReplacementTransform(xaxis,ihatvec))
        self.play(x.animate.next_to(ihatvec,DOWN))

        self.play(y.animate.set_color(GREEN))
        self.play(ReplacementTransform(yaxis,jhatvec))
        self.play(y.animate.next_to(jhatvec,LEFT))

        #convert to vectors
        xvec = MathTex(r"\vec{x}").move_to(x)
        yvec = MathTex(r"\vec{y}").move_to(y)
        xvec[0][1].set_color(RED)
        yvec[0][1].set_color(GREEN)

        self.play(Transform(x,xvec))
        self.play(Transform(y,yvec))

        #linearity
        xvec2 = VGroup(ihatvec.copy(),x.copy()).shift(RIGHT)
        xvec3 = VGroup(ihatvec.copy(),x.copy()).shift(2*RIGHT)
        yvec1 = VGroup(jhatvec.copy(),y.copy()).shift(3*RIGHT)
        yvec2 = VGroup(jhatvec.copy(),y.copy()).shift(3*RIGHT+UP)

        self.play(ReplacementTransform(ihatvec.copy(),xvec2))
        self.play(ReplacementTransform(ihatvec.copy(),xvec3))
        self.play(ReplacementTransform(jhatvec.copy(),yvec1))
        self.play(ReplacementTransform(jhatvec.copy(),yvec2))
        
        #combination
        np2 = NumberPlane().set_opacity(0.4).set_color(BLUE).set_z_index(-1)
        v = np2.get_vector([3,2,0],color=YELLOW)
        vtex = MathTex(r" \vec{v}").set_color(YELLOW).move_to(v).shift(LEFT*0.4+UP*0.4)

        self.play(FadeIn(np2))
        self.play(Write(v))
        self.play(Unwrite(p1))
        self.play(Write(vtex))
        
        vinxy = MathTex(r"\vec{v}",r"=3",r"\vec{x}",r"+2",r"\vec{y}").shift(DOWN*2)
        vinxy[0].set_color(YELLOW)
        vinxy[2][1].set_color(RED)
        vinxy[4][1].set_color(GREEN)
        self.play(Write(vinxy))

        #transition i,j
        self.play(Unwrite(VGroup(xvec2,xvec3,yvec1,yvec2,p1tex,p1tex2,p1)))

        ihat = (MathTex(r"\hat{i}")).move_to(x).set_color(RED)
        jhat = (MathTex(r"\hat{j}")).move_to(y).set_color(GREEN)
        self.play(ReplacementTransform(x,ihat))
        self.play(ReplacementTransform(y,jhat))

        vinij = MathTex(r"\vec{v}",r"=3",r"\hat{i}",r"+2",r"\hat{j}").shift(DOWN*2)
        vinij[0].set_color(YELLOW)
        vinij[2].set_color(RED)
        vinij[4].set_color(GREEN)
        self.play(ReplacementTransform(vinxy,vinij))

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

        self.play(Write(field_equation1))
        self.play(Write(point_example))
        self.play(Circumscribe(field_equation1[1],time_width=5),run_time=4)
        self.play(Write(vector_example))
        self.play(Circumscribe(field_equation1[3],time_width=5),run_time=4)
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

        self.play(Write(axis),Write(labels))
        self.play(Write(p1))
        self.play(Write(field_equation1_example1[0:2]))
        self.play(p1.animate.shift(RIGHT*2 + UP))

        #vector
        ihatvec = Vector(RIGHT,color=RED)
        jhatvec = Vector(UP,color=GREEN)
        ihat = (MathTex(r"\hat{i}")).next_to(ihatvec,DOWN).set_color(RED)
        jhat = (MathTex(r"\hat{j}")).next_to(jhatvec,LEFT).set_color(GREEN)
        vector1 = Vector([2,1],color=YELLOW).shift(RIGHT*2+UP)

        self.play(Write(field_equation1_example1[2]))

        self.play(Write(ihatvec),Write(ihat))
        self.play(Write(jhatvec),Write(jhat))
        self.play(GrowArrow(vector1))


        #second position
        field_equation1_example2 = MathTex(r"\vec{F}",r"(-3,-1.5)",r"=-3\hat{i} -1.5\hat{j}").next_to(field_equation1,DOWN).to_edge(LEFT)
        field_equation1_example2[1][1:3].set_color(PURE_GREEN)
        field_equation1_example2[1][4:8].set_color(PURE_GREEN)
        field_equation1_example2[2][1:3].set_color(YELLOW)
        field_equation1_example2[2][5:9].set_color(YELLOW)

        vector1.add_updater(lambda mob: mob.become(Vector(vecField1(p1))).move_to(p1).shift(p1.get_center() - vector1.get_start()).set_color(YELLOW))

        self.play(ReplacementTransform(field_equation1_example1,field_equation1_example2))
        self.play(p1.animate.move_to([2,-1.5,0]))
        self.play(p1.animate.move_to([-3,-1.5,0]))

        #prepare for full visual
        vector1.suspend_updating()
        self.play(Unwrite(field_equation1_example2),Unwrite(p1),Unwrite(vector1))
        self.play(Unwrite(labels),Unwrite(axis))

        colors1 = [BLUE,GREEN,YELLOW,RED]
        vecField1Func1 = lambda pos: pos[0]*RIGHT + pos[1]*UP
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=6,min_color_scheme_value=1, colors=colors1)

        self.play(Write(vector_field1))

        #streamlines
        stream = StreamLines(vecField1Func1, stroke_width=2, max_anchors_per_line=100, virtual_time=50, n_repeats=5, colors=colors1, min_color_scheme_value=1,  max_color_scheme_value=6)

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
        field_equation2 = MathTex(r"\vec{F}(x,y)=y\hat{i} +0\hat{j}").to_corner(UL).set_z_index(1)
        b1 = SurroundingRectangle(field_equation2,color=BLACK,fill_opacity=1,fill_color=BLACK).move_to(field_equation2).set_z_index(1)
        self.play(Write(VGroup(b1,field_equation2)))

        vecField1Func2 = lambda pos: pos[1]*RIGHT + 0*pos[1]*UP
        vector_field2 = ArrowVectorField(vecField1Func2, max_color_scheme_value=3,min_color_scheme_value=0, colors=colors1).set_z_index(-1)
        self.play(Write(vector_field2))

        #streamlines
        stream = StreamLines(vecField1Func2, stroke_width=2, max_anchors_per_line=100, virtual_time=50, n_repeats=5, colors=colors1, min_color_scheme_value=1,  max_color_scheme_value=3).set_z_index(-1)

        self.play(vector_field2.animate.set_opacity(0.3), run_time=0.1)
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=2)
        self.wait(5)

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
        field_equation3 = MathTex(r"\vec{F}(x,y)=-y\hat{i} +x\hat{j}").to_corner(UL).set_z_index(1)
        b1 = SurroundingRectangle(field_equation3,color=BLACK,fill_opacity=1,fill_color=BLACK).move_to(field_equation3).set_z_index(1)
        self.play(Write(VGroup(b1,field_equation3)))

        vecField1Func3 = lambda pos: -pos[1]*RIGHT + pos[0]*UP
        vector_field3 = ArrowVectorField(vecField1Func3, max_color_scheme_value=6,min_color_scheme_value=1, colors=colors1).set_z_index(-1)
        self.play(Write(vector_field3))

        #streamlines
        stream = StreamLines(vecField1Func3, stroke_width=2, max_anchors_per_line=50, virtual_time=50, n_repeats=1, colors=colors1, min_color_scheme_value=1,  max_color_scheme_value=6).set_z_index(-1)

        self.play(vector_field3.animate.set_opacity(0.3), run_time=0.1)
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=2)
        self.wait(5)

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

# Divergence:
# 3d aanalog
# zurück in magnet und beoabcthung0

#!!!!! corection on value outside not siurrounding is always 0
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
        self.play(Create(vector_field1))
        self.add(stream)
        stream.start_animation(flow_speed=1.4)

        self.play(FadeIn(p1,s1,s2,decnum,c1,div_tex))
        self.play(p1.animate.move_to([2,0,0]))
        self.play(p1.animate.move_to([-2,0,0]))

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
        c1 = Circle(color=WHITE,radius=1)
        div_tex = MathTex(r"div\vec{F}>0")
        div_tex[0][3:5].set_color(YELLOW)
        s1 = SurroundingRectangle(div_tex,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)

        c1.add_updater(lambda mob: mob.move_to(p1))
        div_tex.add_updater(lambda mob: mob.next_to(c1,UP))
        s1.add_updater(lambda mob: mob.move_to(div_tex))

        #fields
        self.play(Create(vector_field1))
        self.add(stream)
        stream.start_animation(flow_speed=1.5)
        self.play(FadeIn(p1,s1,c1,div_tex))
        self.wait(5)

# nabla 
# version div Form
# 2nd law and end

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
        c1 = Circle(color=WHITE,radius=1)
        div_tex = MathTex(r"div\vec{B}=0")
        div_tex[0][3:5].set_color(YELLOW)
        s1 = SurroundingRectangle(div_tex,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)

        c1.add_updater(lambda mob: mob.move_to(p1))
        div_tex.add_updater(lambda mob: mob.next_to(c1,UP))
        s1.add_updater(lambda mob: mob.move_to(div_tex))

        self.play(Write(magnet),FadeIn(vector_field))
        self.add(stream)
        stream.start_animation(flow_speed=4)
        self.play(FadeIn(p1,s1,c1,div_tex))
        self.play(p1.animate.move_to([2,0,0]))
        self.play(p1.animate.move_to([-2,3,0]))

class Nabla2ndLaw(Scene):
    def construct(self):
        
        # Gauss's law for magnetism
        div_tex = MathTex(r"2.div",r"\vec{B}",r"=0")
        div_tex[1].set_color(YELLOW)
        div_formula = MathTex(r"2.\nabla \cdot",r"\vec{B}",r"=0").shift(UP*2)
        div_formula[1].set_color(YELLOW)


        self.play(Write(div_tex))
        self.play(Write(div_formula))
        self.play(div_tex.animate.to_corner(UL), div_formula.animate.to_corner(UR))

        # Nabla operator intro
        nabla_tex = MathTex(r"\nabla").scale(2).shift(UP)
        nabla_word = Tex("Nabla-Operator").next_to(nabla_tex, DOWN)

        self.play(Write(nabla_tex))
        self.play(Write(nabla_word))

        # Show components
        nabla_components = MathTex(r"\nabla=\left [ \frac{\partial}{\partial x},\frac{\partial}{\partial y} \right ]").shift(DOWN*2)

        self.play(Write(nabla_components))
        self.play(FadeOut(VGroup(nabla_tex,nabla_word,nabla_components)))

        # Magnetic field formula
        magnet_field1 = MathTex(r"\vec{B}",r"(x,y) = ",r"\frac{y-s}{x^2+(y-s)^2}",r"\hat{i}",r"- \frac{y+s}{x^2+(y+s)^2}",r"\hat{i}").shift(DOWN*-1.5).to_edge(LEFT)
        magnet_field2 = MathTex(r"\frac{-x}{x^2+(y-s)^2}",r"\hat{j}",r"+ \frac{x}{x^2+(y+s)^2}",r"\hat{j}").shift(DOWN*0.5).to_edge(LEFT)

        magnet_field1[0].set_color(YELLOW)
        self.play(Write(magnet_field1))
        self.play(Write(magnet_field2))

        equation = MathTex(r"\nabla \cdot \vec{B} = \frac{\partial}{\partial x} \cdot \vec{B}_x + \frac{\partial}{\partial y} \cdot \vec{B}_y").shift(DOWN*3).to_edge(LEFT)

        self.play(Write(equation))

        # # Divergence as dot product
        # div_intro = Tex("Divergenz:").shift(DOWN*1.5).to_edge(LEFT)
        # div_formula = MathTex(r"\nabla \cdot \vec{F}").shift(DOWN*1.5).next_to(div_intro, RIGHT)
        # div_formula[0][0].set_color(YELLOW)
        # div_formula[0][2:4].set_color(GREEN)

        # self.play(Write(div_intro))
        # self.play(Write(div_formula))
        # self.play(Circumscribe(div_formula))

        # # Connection back to magnetic field
        # self.play(FadeOut(nabla_components, nabla_word))
        # self.play(nabla_tex.animate.scale(1.4).move_to([0, 0, 0]))

        # gauss_law = MathTex(r"\nabla \cdot \vec{B} = 0").shift(DOWN*3)
        # gauss_law[0][0].set_color(YELLOW)
        # gauss_law[0][2:4].set_color(BLUE)

        # self.play(ReplacementTransform(div_formula.copy(), gauss_law))
        # self.play(Write(gauss_law))

        # # Explain meaning
        # meaning = Tex("Magnetische Monopole existieren nicht").shift(DOWN*4.5).scale(0.9)

        # self.play(Write(meaning))
        # self.wait(2)



# GausOverview
# div explain
# desmos die 2 anderen
# intro int form
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

        self.play(Write(dif_tex), Write(differential_form))

        func1 = lambda pos: 3*(pos[0]/(pos[0]**2 + pos[1]**2 +0.0001)) * RIGHT + 3*(pos[1]/(pos[0]**2 + pos[1]**2 +0.0001)) * UP
        vector_field = ArrowVectorField(func1,x_range=[-3,3],y_range=[-1.5,2.5]).move_to([3.5,0.2,0])

        core = Circle(radius=0.4,color=RED,fill_opacity=1)
        corss1 = Rectangle(height=0.02,width=0.4,fill_opacity=1)
        corss2 = Rectangle(height=0.4,width=0.02,fill_opacity=1)
        proton = VGroup(core,corss1,corss2).scale(0.8).move_to([3.5,-0.2,0])

        b1 = SurroundingRectangle(vector_field,color=WHITE)

        self.play(FadeIn(b1))
        self.play(FadeIn(proton))
        self.play(FadeIn(vector_field))

        self.play(Write(int_tex), Write(integral_form))
        self.play(Write(word_tex), Write(word_form))





















class Gauss(ThreeDScene):
    def construct(self):

        #charge
        charge = Dot3D(color=RED).scale(2)

        self.move_camera(phi=60*DEGREES, zoom=3)
        self.begin_ambient_camera_rotation(rate=0.5)

        #vectors
        a1 = Arrow3D(start=ORIGIN, end=[0,0,1],resolution=5,height=0.01,base_radius=0.04)
        a2 = Arrow3D(start=ORIGIN, end=[0,0,-1],resolution=5,height=0.01,base_radius=0.04)
        a3 = Arrow3D(start=ORIGIN, end=[1,0,0],resolution=5,height=0.01,base_radius=0.04)
        a4 = Arrow3D(start=ORIGIN, end=[-1,0,0],resolution=5,height=0.01,base_radius=0.04)
        a5 = Arrow3D(start=ORIGIN, end=[0,1,0],resolution=5,height=0.01,base_radius=0.04)
        a6 = Arrow3D(start=ORIGIN, end=[0,-1,0],resolution=5,height=0.01,base_radius=0.04)

        arrows = VGroup(a1,a2,a3,a4,a5,a6).set_color(RED)
        self.add(charge)
        self.add(arrows)
        self.wait(1)

        #surface
        sphere = Sphere(resolution=(24,12))

        self.play(arrows.animate.scale(2))
        self.play(Create(sphere))

        #Law
        law_tex = MathTex(r"\oint_{A}\vec{E}\cdot d\vec{A}").move_to([0,0,2])

        self.add_fixed_orientation_mobjects(law_tex)
        self.add_fixed_in_frame_mobjects(law_tex)
        self.play(Write(law_tex))
        self.wait()

class VectorDotProductLabel(Scene):
    def construct(self):

        dotproduct2 = MathTex(r"\vec{v}",r"\cdot",r"\vec{w}").scale(1.7)
        dotproduct2[0].set_color(YELLOW)
        dotproduct2[2].set_color(BLUE)

        dotproduct = Tex("Skalarprodukt").shift(UP*2)
        ar1 = Arrow(dotproduct.get_bottom(), dotproduct2[1].get_top())


        #dot product intro
        self.play(Write(dotproduct2))
        self.play(Write(dotproduct), GrowArrow(ar1))
        self.play(Circumscribe(dotproduct2[1]))
        self.play(Indicate(dotproduct2[1]))
        self.play(Unwrite(ar1))

        #numberplane visual
        number_plane = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-5, 5, 1),
            x_length=4,
            y_length=4,
        ).move_to(LEFT*4.5).set_opacity(0.7)
        npV1 = number_plane.get_vector([3,2,0]).set_color(YELLOW)
        npW1 = number_plane.get_vector([4,1,0]).set_color(BLUE)

        self.play(Write(number_plane))
        self.play(ReplacementTransform(dotproduct2[0].copy(),npV1))
        self.play(ReplacementTransform(dotproduct2[2].copy(),npW1))

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
        self.play(Write(cdot))
        self.play(ReplacementTransform(dotproduct2[2].copy(),vectorw))

        #calc right side
        equals = MathTex(r"=").shift(2*DOWN+RIGHT*2)
        equation = MathTex(r"3\cdot 4",r"+",r"2\cdot1").shift(2*DOWN+RIGHT*4)
        equation[0].set_color(RED)
        equation[2].set_color(GREEN)
        equationCopy1 = VGroup(vectorv[0][1],vectorw[0][1]).copy()
        equationCopy2 = VGroup(vectorv[0][2],vectorw[0][2]).copy()

        self.play(Write(equals))
        self.play(ClockwiseTransform(equationCopy1,equation[0]))
        self.play(FadeIn(equation[1]))
        self.play(ClockwiseTransform(equationCopy2,equation[2]))

        #numberplane visual2
        npV2 = number_plane.get_vector([-4,4,0]).set_color(YELLOW)
        npW2 = number_plane.get_vector([-1,-3,0]).set_color(BLUE)

        self.play(ReplacementTransform(npV1,npV2))
        self.play(ReplacementTransform(npW1,npW2))

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
        self.play(ReplacementTransform(dotproduct2[2].copy(),vectorw2))

        #calc right side
        equationCopy3 = VGroup(vectorv2[0][1:3],vectorw2[0][1:3]).copy()
        equationCopy4 = VGroup(vectorv2[0][3],vectorw2[0][3]).copy()
        equation2 = MathTex(r"-4\cdot -1",r"+",r"4\cdot -3").shift(2*DOWN+RIGHT*4)
        equation2[0].set_color(RED)
        equation2[2].set_color(GREEN)

        self.play(ClockwiseTransform(equationCopy3,equation2[0]))
        self.play(FadeIn(equation2[1]))
        self.play(ClockwiseTransform(equationCopy4,equation2[2]))

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
        self.play(FadeIn(nump))
        self.play(GrowArrow(v_vec), FadeIn(v_vectex))
        self.play(GrowArrow(w_vec), FadeIn(w_vectex))
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

        self.play(GrowFromCenter(line))
        self.play(Indicate(VGroup(v_vec,v_vectex)))
        self.play(Write(conetctLine))
        self.play(ReplacementTransform(w_vec.copy(),projectVector))
        self.play(GrowFromPoint(rightan, projectVector.get_end()))

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

        self.play(w_vec.animate.rotate_about_origin(PI))
        self.play(Indicate(eqation1))
        self.play(TransformMatchingShapes(eqation1,eqation2))

        self.play(w_vec.animate.rotate_about_origin(PI+0.6435))
        self.play(Indicate(eqation2))
        self.play(TransformMatchingShapes(eqation2,eqation3))

        #rotation and calc
        dotp = ValueTracker()
        dotp.add_updater(lambda mob: mob.set_value(4*(projectVector.get_x()*v_vec.get_x() + projectVector.get_y()*v_vec.get_y())))
        number = DecimalNumber(0,num_decimal_places=2).next_to(eqation3[3], RIGHT, buff=0.4)
        number.add_updater(lambda mob: mob.set_value(dotp.get_value()))

        self.add(dotp)
        self.play(FadeOut(eqation3[4]))
        self.play(FadeIn(number))

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
        self.play(Write(positive_plate),Write(positive_plate2))
        self.play(Write(negativ_plate), Write(negativ_plate2))
        self.play(AnimationGroup(GrowArrow(fieldLines[0]),GrowArrow(fieldLines[1]),GrowArrow(fieldLines[2]),GrowArrow(fieldLines[3]),GrowArrow(fieldLines[4]), lag_ratio=0.7), run_time=1)

        #introduce surface
        plane_surface = Rectangle(height=4,width=0.25,fill_opacity=1,color=BLUE).set_z_index(1)
        plane_surface2 = Polygon(plane_surface.get_corner(UR),plane_surface.get_corner(DR),plane_surface.get_corner(DR)+[0.2,0.4,0],plane_surface.get_corner(UR)+[0.2,-0.4,0],fill_opacity=1,color=DARK_BLUE).set_z_index(-1)

        self.play(VGroup(negativ_plate,negativ_plate2).animate.shift(RIGHT*2))
        self.play(Write(plane_surface),Write(plane_surface2))

        #show flux
        flux_tex = Tex("Fluss").shift(UP*3).scale(1.5)
        func1 = lambda pos: RIGHT
        stream = StreamLines(func1, stroke_width=4, max_anchors_per_line=25, virtual_time=50, n_repeats=15,
                             x_range=[-5.7,5,7],y_range=[-2,2])

        self.play(Write(flux_tex))
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=5)
        self.wait(5)

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

        self.play(ReplacementTransform(forumla[0][2].copy(),vecE))
        self.play(ReplacementTransform(forumla[0][4].copy(),area))
        self.play(Write(normal_vector_tex), GrowArrow(normal_vector))

        self.play(vecE.animate.next_to(e_vector,UP).set_color(GREEN))
        self.play(GrowArrow(e_vector))

        #new formula
        forumla2 = MathTex(r"\phi = \vec{E} \cdot \hat{n} \cdot A").shift(UP*3)
        forumla2[0][2:4].set_color(GREEN)
        forumla2[0][5:7].set_color(RED)
        forumla2[0][8].set_color(BLUE)
        normal_vector_tex.add_updater(lambda mob: mob.next_to(normal_vector,DOWN))

        self.play(normal_vector.animate.rotate_about_origin(PI/4), VGroup(plane_surface,plane_surface2).animate.rotate_about_origin(PI/4))
        self.play(ReplacementTransform(forumla,forumla2))

        #rotate change
        forumla3 = MathTex(r"\phi = \vec{E} \cdot \hat{n} \cdot A=").shift(UP*3).align_to(forumla2,LEFT)
        forumla3[0][2:4].set_color(GREEN)
        forumla3[0][5:7].set_color(RED)
        forumla3[0][8].set_color(BLUE)

        angle = ValueTracker(PI/4)
        value = DecimalNumber(0.707,num_decimal_places=2).next_to(forumla3,RIGHT)
        value.add_updater(lambda mob: mob.set_value(np.cos(angle.get_value())))

        self.play(TransformMatchingShapes(forumla2,forumla3))
        self.play(Write(value))
        self.play(VGroup(plane_surface,plane_surface2,normal_vector).animate.rotate_about_origin(PI/4),angle.animate.set_value(PI/2))
        self.play(VGroup(plane_surface,plane_surface2,normal_vector).animate.rotate_about_origin(PI/2),angle.animate.set_value(PI))
        self.play(VGroup(plane_surface,plane_surface2,normal_vector).animate.rotate_about_origin(PI/2),angle.animate.set_value(3*PI/2))
        self.play(VGroup(plane_surface,plane_surface2,normal_vector).animate.rotate_about_origin(3*PI/8),angle.animate.set_value(15*PI/8))

        #surface element
        surface_element = MathTex(r"\vec{A}=\hat{n}\cdot A").shift(UP*3).next_to(plane_surface,LEFT)
        forumla4 = MathTex(r"\phi = \vec{E} \cdot \vec{A}").shift(UP*3).align_to(forumla2,LEFT)
        forumla4[0][2:4].set_color(GREEN)
        forumla4[0][5:7].set_color(RED)

        self.play(Write(surface_element))
        self.play(ReplacementTransform(forumla3,forumla4), FadeOut(value))

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
        self.play(Write(labels))
        self.play(Indicate(graph))

        sq = MathTex(r"s=?").to_edge(UP)
        svt = MathTex(r"s=v\cdot t").to_edge(UP)
        svt[0][2].set_color(GREEN)
        svt[0][4].set_color(YELLOW)

        #frage
        self.play(Write(sq))
        self.play(ReplacementTransform(sq,svt))

        #Lösung
        self.play(Write(dftex))
        self.play(Write(dxtex))
        self.play(Write(equation))
        self.play(Unwrite(svt))

        #observation
        self.play(FadeIn(rect))
        self.play(Write(bracedf))
        self.play(Write(bracedx))

        #area
        area = MathTex(r"[",r"A",r"]",r"=\frac{m}{s}\cdot s=m").move_to(rect)
        area[0][2:5].set_color(GREEN)
        area[0][6:7].set_color(YELLOW)

        self.play(Write(area[1]))
        self.play(Write(area[0]),Write(area[2:]))

        aiss = MathTex(r"s=A").next_to(equation, DOWN).align_to(equation,LEFT)
        self.play(Write(aiss))
        self.play(Indicate(aiss))

        #bezug integral
        integral = MathTex(r"s=\int_{}^{}2\frac{m}{s}\cdot 5s=10m").next_to(aiss,DOWN).to_edge(RIGHT)
        self.play(Write(integral))

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
        self.play(Write(axes),Write(graph1),Write(vtex),Write(ttex))
        self.play(Write(rect1), run_time=1)

        #area
        self.play(Write(area))
        self.play(Write(a1))

        #area2
        self.play(ReplacementTransform(graph1,graph2),ReplacementTransform(rect1,rect2))
        self.play(ReplacementTransform(a1,a2))

        #area3 no solution
        self.play(ReplacementTransform(graph2,graph3),ReplacementTransform(rect2,rect3))
        self.play(ReplacementTransform(a2,a3))

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
        self.play(Create(graph))
        self.play(Write(axes), Write(labels))
        self.play(Write(area))
        self.add(finer_rects)
        self.play(opacity.animate.set_value(0.7))

        #show overlap
        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        self.play(GrowArrow(arrow3))

        #show smaller rectangles
        self.play(Unwrite(arrows))
        self.play(d.animate.set_value(0.5), run_time=2)
        self.play(d.animate.set_value(0.25), run_time=2)
        self.play(d.animate.set_value(0.1), run_time=2)
        self.play(d.animate.set_value(0.01), opacity.animate.set_value(1), run_time=2)

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
        self.play(Create(graph))
        self.play(Write(axes), Write(labels))
        self.play(Write(rect))

        #df dx
        self.play(Write(brace_dx))
        self.play(Write(dx_tex))
        self.play(Write(brace_fx))
        self.play(Write(VGroup(fx_tex,b1)))

        #area def
        self.play(Write(VGroup(A_tex,b2)))
        self.play(ReplacementTransform(A_tex.copy(),A_calc[0]))
        self.play(ReplacementTransform(fx_tex.copy(),A_calc[1]), Write(A_calc[2]))
        self.play(ReplacementTransform(dx_tex.copy(),A_calc[3]))

        #hop over rectangles
        self.play(brace_dx.animate.become(Brace(rect[1],DOWN)), brace_fx.animate.become(Brace(rect[1],LEFT)), A_tex.animate.move_to(rect[1]))
        self.play(brace_dx.animate.become(Brace(rect[2],DOWN)), brace_fx.animate.become(Brace(rect[2],LEFT)), A_tex.animate.move_to(rect[2]))
        self.play(brace_dx.animate.become(Brace(rect[3],DOWN)), brace_fx.animate.become(Brace(rect[3],LEFT)), A_tex.animate.move_to(rect[3]))

        #meaning of A
        self.play(Unwrite(VGroup(brace_dx,brace_fx,fx_tex,dx_tex,b1,b2,A_tex)))
        self.play(ReplacementTransform(A_calc, awords))

        dA1 = MathTex(r"dA").move_to(rect[0])
        dA2 = MathTex(r"dA").move_to(rect[1])
        dA3 = MathTex(r"dA").move_to(rect[2])
        dA4 = MathTex(r"dA").move_to(rect[3])
        self.play(Write(VGroup(dA1,dA2,dA3,dA4)))
        self.play(AnimationGroup(dA1.animate.move_to(awords[0]).set_opacity(0),
                                 dA2.animate.move_to(awords[0]).set_opacity(0),
                                 dA3.animate.move_to(awords[0]).set_opacity(0),
                                 dA4.animate.move_to(awords[0]).set_opacity(0),lag_ratio=0.8))

        #int explain
        self.play(awords[1][0][0:5].animate.set_color(YELLOW))
        self.play(Write(A_word4))
        self.play(ReplacementTransform(A_word4, A_calc2))
        self.play(ReplacementTransform(A_calc2.copy(), A_calc3))

        #add domain
        x0 = MathTex(r"x=1").shift(LEFT*3.5+DOWN*3)
        x1 = MathTex(r"x=5").shift(LEFT*-5.7+DOWN*3)
        x0[0][2].set_color(YELLOW)
        x1[0][2].set_color(YELLOW)

        self.play(Write(x0))
        self.play(Write(x1))
        self.play(Unwrite(VGroup(A_calc2,awords)))
        self.play(A_calc3.animate.move_to([0,2,0]))
        self.play(ReplacementTransform(A_calc3,A_calc4), x0.copy().animate.move_to(A_calc4).set_opacity(0),
                   x1.copy().animate.move_to(A_calc4).set_opacity(0))

class FluxIntegral(ThreeDScene):
    def construct(self):
        
        #known setup
        surface = Rectangle(width=4,height=4,color=BLUE,fill_opacity=1)
        area = MathTex(r"A").set_color(BLUE).shift(LEFT*3)
        formula = MathTex(r"\phi=",r"\vec{E}",r"\cdot",r"\vec{A}").shift(UP*3)
        formula[1].set_color(GREEN)
        formula[3].set_color(RED)

        self.play(DrawBorderThenFill(surface))
        self.play(Write(area))
        self.play(Write(formula))

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
        self.play(VGroup(rect,da).animate.scale(0.01))
        self.play(VGroup(rect,da).animate.scale(100))

        self.play(Write(surface_elementOld))
        self.play(ReplacementTransform(surface_elementOld.copy(),surface_element))

        self.play(Circumscribe(formula))
        self.play(ReplacementTransform(formula,formula2))


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

        self.play(Circumscribe(formula2[0][0:2]))
        self.play(ReplacementTransform(formula2,formula3))

        self.play(FadeOut(rect))
        self.play(da.animate.next_to(surface,DOWN))
        self.play(LaggedStart( *[FadeIn(tile, scale=0.5) for tile in dA_tiles], lag_ratio=0.02))

        #integral cancel
        self.play(Circumscribe(formula3[0][0:4]))
        self.play(FadeOut(formula3[0][0:3]))

        #realise complexity
        self.play(dA_tiles.animate.set_opacity(0),FadeOut(da))
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
        self.play(ReplacementTransform(formula3[0][5:7], closed_int))
        self.wait()

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

        self.play(Write(formula))
        self.play(formula.animate.to_corner(UL))
        self.play(Create(proton))
        self.play(Write(circle))

        #sphere
        sphere = Sphere().rotate(PI/4,axis=RIGHT).scale(2.5)
        self.play(Create(sphere))
        self.play(Rotate(sphere, PI, axis=UP))
        self.play(sphere.animate.shift(-5.5*RIGHT+2*DOWN).scale(1/2.5))

        #r is n 
        da = MathTex(r"d",r"\vec{A}",r"=",r"\hat{n}",r"\cdot",r"A").shift(UP*3)
        da[3].set_color(RED)
        n_vec = Vector([1,0]).next_to(circle,RIGHT,buff=0).set_color(RED)
        nhat = MathTex(r"\hat{n}").next_to(n_vec,UP).set_color(RED)

        r_vec = Vector([2.1,0]).next_to(core,RIGHT,buff=0).set_color(YELLOW)
        rhat = MathTex(r"\vec{r}").next_to(r_vec,UP).set_color(YELLOW)       
        risn = MathTex(r"\hat{r}",r"=",r"\hat{n}").move_to([4,2,0])       
        risn[0].set_color(YELLOW)
        risn[2].set_color(RED)

        self.play(ReplacementTransform(formula[3].copy(),da))
        self.play(ReplacementTransform(da[3].copy(),nhat),GrowArrow(n_vec))
        self.play(Write(rhat),GrowArrow(r_vec))

        self.play(Write(risn))
        self.play(Rotate(VGroup(nhat,rhat,n_vec,r_vec),2*PI,about_point=ORIGIN))

        #reinsert
        da2 = MathTex(r"d\vec{A}=",r"\hat{r}",r"\cdot A").shift(UP*3)
        da2[1].set_color(YELLOW)

        self.play(FadeOut(da),ReplacementTransform(risn,da2))
        self.play(FadeOut(VGroup(circle,rhat,r_vec,nhat,n_vec)))

        self.play(FadeOut(da2[0]),FadeOut(formula[3]))
        self.play(formula[0:3].animate.next_to(da2[1],LEFT).shift(DOWN*0.07))

        #constants
        e_con = MathTex(r"E").shift(UP*1)
        formula2 = MathTex(r"\oint_{A}",r"A").shift(UP*3)

        self.play(FadeOut(proton))
        self.play(VGroup(formula[1:3],da2[1]).animate.shift(DOWN*2))

        self.play(ReplacementTransform(VGroup(formula[1:3],da2[1]), e_con))
        self.play(e_con.animate.shift(UP*2))
        self.play(e_con.animate.shift(LEFT*1), FadeOut(VGroup(formula,da2)), FadeIn(formula2))

        #back to sphere
        self.play(sphere.animate.move_to([0,-0.7,0]))
        self.play(sphere.animate.scale(2.5))

        #area
        area = MathTex(r"A=",r"4\pi r^{2}").move_to([5,0,0])
        area2 = MathTex(r"4\pi r^{2}").move_to(area[1])
        self.play(Write(area))
        self.play(area2.animate.move_to(formula2), FadeOut(formula2))

        #coulomb
        formula3 =  MathTex(r"\phi=E\cdot 4\pi r^{2}").shift(UP*3)
        coulomb = MathTex(r"E=\frac{1}{4\pi \varepsilon_{0}} \cdot \frac{q}{r^{2}}").to_corner(UR)
        solution = MathTex(r"\phi=\frac{q}{\varepsilon_{0}}").shift(UP*3)

        self.play(FadeOut(VGroup(formula2,area2, e_con, area)), FadeIn(formula3))
        self.play(Write(coulomb))
        self.play(ReplacementTransform(formula3,solution))

        #show flux
        vecField1Func1 = lambda pos: pos[0]*RIGHT + pos[1]*UP
        colors1 = [ORANGE,RED]
        stream = StreamLines(vecField1Func1, stroke_width=2, max_anchors_per_line=50, virtual_time=50, n_repeats=1, colors=colors1, min_color_scheme_value=1,  max_color_scheme_value=6).set_z_index(-99)

        self.play(FadeOut(coulomb))
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=2)
        self.wait(5)

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

        vecField1Func2 = lambda pos: -pos[0]*RIGHT + -pos[1]*UP
        colors2 = [GREEN,PURE_GREEN]
        stream2 = StreamLines(vecField1Func2, stroke_width=2, max_anchors_per_line=50, virtual_time=50, n_repeats=1, colors=colors2, min_color_scheme_value=1,  max_color_scheme_value=6).set_z_index(-99)
        stream2.start_animation(warm_up=True, flow_speed=2)

        self.wait(5)

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
        self.play(Write(square))
        self.play(Write(proton))
        self.move_camera(phi=60*DEGREES,theta=-45*DEGREES)


        #field stretch
        func0 = lambda pos: pos[0]*RIGHT + pos[1]*UP
        f0 = ArrowVectorField(func=func0,color=RED).set_opacity(0.7).set_z_index(-2)

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
 
# core = Circle(radius=0.4,color=RED,fill_opacity=1)
# corss1 = Rectangle(height=0.02,width=0.4,fill_opacity=1)
# corss2 = Rectangle(height=0.4,width=0.02,fill_opacity=1)
# proton = VGroup(core,corss1,corss2).shift(LEFT*2)

# core1 = Circle(radius=0.4,color=PURE_GREEN,fill_color=PURE_GREEN,fill_opacity=1)
# corss3 = Rectangle(height=0.03,width=0.3,fill_opacity=1)
# electron = VGroup(core1,corss3).shift(RIGHT*2)

# self.add(proton,electron)

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

        def vecField3(pos):
            e = 0.001
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = np.sin(0.5*(x+y))
            field[1] = np.cos(0.5*(x-y))
            return field[0]*RIGHT + field[1]*UP

        def curlFunc1(x,y):
            xcomp = np.sin(0.5*x - 0.5*y)
            ycomp = np.cos(0.5*x + 0.5*y)
            return -0.5*(xcomp + ycomp)


        colors1 = [BLUE,GREEN,YELLOW,RED]
        vecField1Func1 = lambda pos: vecField1(pos=pos)
        vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=8,min_color_scheme_value=1, colors=colors1).set_z_index(-1)
        vector_field3 = ArrowVectorField(vecField1Func1, max_color_scheme_value=1.25,min_color_scheme_value=0.5, colors=colors1).set_z_index(-1)
        self.add(vector_field1)

        p1 = Dot().scale(0.5)
        c1 = Circle(color=WHITE,radius=0.2)
        div_tex = MathTex(r"rot\vec{F}=")
        div_tex[0][3:5].set_color(YELLOW)
        decnum = DecimalNumber(0)
        s1 = SurroundingRectangle(div_tex,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)
        s2 = SurroundingRectangle(decnum,color=BLACK, fill_color=BLACK ,fill_opacity=1, stroke_width=0)

        c1.add_updater(lambda mob: mob.move_to(p1))
        div_tex.add_updater(lambda mob: mob.next_to(p1,UP))
        s1.add_updater(lambda mob: mob.move_to(div_tex))
        s2.add_updater(lambda mob: mob.move_to(decnum))
        decnum.add_updater(lambda mob: mob.set_value(curlFunc1(p1.get_x(),p1.get_y())).next_to(p1,UP).shift(RIGHT*1.5))


        self.add(p1,s1,s2,decnum,c1,div_tex)
        self.play(p1.animate.move_to([-6,4,0]))
        self.play(p1.animate.move_to([6,4,0]))
        self.play(p1.animate.move_to([6,3,0]))
        self.play(p1.animate.move_to([-6,3,0]))
        self.play(p1.animate.move_to([-6,2,0]))
        self.play(p1.animate.move_to([6,2,0]))
        self.play(p1.animate.move_to([6,1,0]))
        self.play(p1.animate.move_to([-6,1,0]))
        self.play(p1.animate.move_to([-6,0,0]))
        self.play(p1.animate.move_to([6,0,0]))
        self.play(p1.animate.move_to([6,-1,0]))
        self.play(p1.animate.move_to([-6,-1,0]))
        self.play(p1.animate.move_to([-6,-2,0]))
        self.play(p1.animate.move_to([6,-2,0]))
        self.play(p1.animate.move_to([6,-3,0]))
        self.play(p1.animate.move_to([-6,-3,0]))
        self.play(p1.animate.move_to([-6,-4,0]))
        self.play(p1.animate.move_to([6,-4,0]))

class Curl3D(ThreeDScene):
    def construct(self):

        def vecField1(pos):
            e = 0.001
            x = pos[0]
            y = pos[1]
            field = [0,0]
            field[0] = -y
            field[1] = x
            return field[0]*RIGHT + field[1]*UP

        colors1 = [BLUE,GREEN,YELLOW,RED]
        vecField1Func1 = lambda pos: vecField1(pos=pos)
        # vector_field1 = ArrowVectorField(vecField1Func1, max_color_scheme_value=6,min_color_scheme_value=1, colors=colors1,
        #                                  x_range=[-6,6], y_range=[-6,6]).set_z_index(-1)
        vector_field2 = ArrowVectorField(vecField1Func1, max_color_scheme_value=6,min_color_scheme_value=1, colors=colors1,
                                         x_range=[-6,6,2], y_range=[-6,6,2]).set_z_index(-1)
        
        axis = ThreeDAxes(x_range=[-2,2,1],y_range=[-2,2,1],z_range=[0,0.01,0.01],x_length=12,y_length=12,z_length=0.01,z_axis_config={"include_tip": False})

        ihat = Arrow3D(start=ORIGIN,end=[2,0,0]).set_color(PURE_RED)
        jhat = Arrow3D(start=ORIGIN,end=[0,2,0]).set_color(PURE_GREEN)
        khat = Arrow3D(start=ORIGIN,end=[0,0,2]).set_color(PURE_BLUE).set_z_index(99)

        ihat_tex = MathTex(r"\hat{i}").set_color(PURE_RED).move_to([1,-1,0]).rotate(PI/2,axis=OUT)
        jhat_tex = MathTex(r"\hat{j}").set_color(PURE_GREEN).move_to([1,1,0])
        khat_tex = MathTex(r"\hat{k}").set_color(PURE_BLUE).move_to([-1,0,1]).rotate(PI/2,axis=RIGHT).rotate(PI/2,axis=OUT)

        # self.add()
        self.add(axis,khat,ihat,jhat,khat_tex,ihat_tex,jhat_tex)
        self.move_camera(phi=60*DEGREES, theta=-45*DEGREES)
        self.move_camera(zoom=2.5,frame_center=[0,0,0.3])
        # self.play(ReplacementTransform(vector_field1,vector_field2))


        #streamlines
        stream = StreamLines(vecField1Func1, stroke_width=2, max_anchors_per_line=50, virtual_time=50, n_repeats=1, colors=colors1, min_color_scheme_value=1,  max_color_scheme_value=6).set_z_index(-99)

        self.play(vector_field2.animate.set_opacity(0.3), run_time=0.1)
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=2)
        self.wait(5)

class Circulation(Scene):
    def construct(self):
        1
