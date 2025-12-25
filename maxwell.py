from manim import *


class T(Scene):
    def construct(self):
        max_x = 6
        max_y = 6
        step = 0.5
        e = 0.001
        scalar = 1
        
        # func1 = lambda pos: 0.3*pos[0] * RIGHT + 0.3*pos[1] * UP
        # func1 = lambda pos: -1*pos[1]/(np.sqrt(pos[0]**2 + pos[1]**2)) * RIGHT + 1*pos[0]/(np.sqrt(pos[0]**2 + pos[1]**2)) * UP
        # func1 = lambda pos: -1*pos[1] * RIGHT + 1*pos[0] * UP
        # func1 = lambda pos: 3*pos[0]*pos[1]/((pos[0]**2 + pos[1]**2)**2 + e) * RIGHT + (2*pos[1]**2 - pos[0]**2)/((pos[0]**2 + pos[1]**2)**2 + e) * UP
        func1 = lambda pos: scalar*((pos[1]-1)*RIGHT + -pos[0]*UP)/(pos[0]**2+(pos[1]-1)**2+e) + scalar*((-(pos[1]+1))*RIGHT + pos[0]*UP)/(pos[0]**2+(-(pos[1]+1))**2+e)

        # vector_field = ArrowVectorField(func1, x_range=[-max_x, max_x, step], y_range=[-max_y, max_y, step])
        
        stream = StreamLines(func1, stroke_width=2, max_anchors_per_line=300, virtual_time=50, n_repeats=5)

        self.add(NumberPlane())
        # self.add(vector_field)
        self.add(stream)
        stream.start_animation(warm_up=False, flow_speed=2.5)
        self.wait(5)

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
        vectorw2 = MathTex(r"\begin{bmatrix}-1\\3\end{bmatrix}").shift(2*DOWN+RIGHT)
        vectorw2[0][0].set_color(BLUE)
        vectorw2[0][4].set_color(BLUE)
        vectorw2[0][1:3].set_color(RED)
        vectorw2[0][3].set_color(GREEN)

        self.play(Unwrite(VGroup(vectorv,vectorw)))
        self.play(Unwrite(equationCopy1),Unwrite(equationCopy2), Unwrite(equation))
        self.play(ReplacementTransform(dotproduct2[0].copy(),vectorv2))
        self.play(ReplacementTransform(dotproduct2[2].copy(),vectorw2))

        #calc right side
        equationCopy3 = VGroup(vectorv2[0][1:3],vectorw2[0][1:3]).copy()
        equationCopy4 = VGroup(vectorv2[0][3],vectorw2[0][3]).copy()
        equation2 = MathTex(r"-4\cdot -1",r"+",r"4\cdot3").shift(2*DOWN+RIGHT*4)
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





class VectorFieldIntro(Scene):
    def construct(self):

        max_x = 16
        max_y = 9
        step = 0.5
        e = 0.001
        scalar = 1

        def vecField1(point: Dot):
            x = point.get_x()
            y = point.get_y()
            field = [0,0]
            field[0] = x
            field[1] = y
            return field
    
        def vecField2(point: Dot):
            x = point.get_x()
            y = point.get_y()
            field = [0,0]
            field[0] = y
            field[1] = 0
            return field

        def vecField3(point: Dot):
            x = point.get_x()
            y = point.get_y()
            field = [0,0]
            field[0] = -y
            field[1] = x
            return field
        


        field_equation2 = MathTex(r"\vec{F}(x,y)=y\hat{i} +0\hat{j}").to_corner(UL)
        field_equation3 = MathTex(r"\vec{F}(x,y)=-y\hat{i} +x\hat{j}").to_corner(UL)

        # field_equation1_example2 = MathTex(r"\vec{F}(-3,-1.5)").next_to(field_equation1,DOWN).to_edge(LEFT)






        # vecField1Func1 = lambda pos: pos[0]*RIGHT + pos[1]*UP
        # vecField1Func2 = lambda pos: pos[1]*RIGHT + 0*pos[1]*UP
        # vecField1Func3 = lambda pos: -pos[1]*RIGHT + pos[0]*UP
        # colors = [BLUE,GREEN,YELLOW,RED]
        # vector_field1 = ArrowVectorField(vecField1Func1, x_range=[-max_x, max_x, step], y_range=[-max_y, max_y, step], max_color_scheme_value=6,min_color_scheme_value=1, colors=colors)
        # vector_field2 = ArrowVectorField(vecField1Func2, x_range=[-max_x, max_x, step], y_range=[-max_y, max_y, step], max_color_scheme_value=3,min_color_scheme_value=0, colors=colors)
        # vector_field3 = ArrowVectorField(vecField1Func3, x_range=[-max_x, max_x, step], y_range=[-max_y, max_y, step], max_color_scheme_value=6,min_color_scheme_value=1, colors=colors)

        #init
        nump = NumberPlane().set_opacity(0.7)
        field_equation1 = MathTex(r"\vec{F}(x,y)=x\hat{i} +y\hat{j}")

        self.play(Write(nump))
        self.play(Write(field_equation1))
        self.play(field_equation1.animate.to_corner(UL))

        #point
        axis = Axes(x_length=12, y_length=7, x_range=[-1,1,10], y_range=[-1,1,10])
        x_label = MathTex(r"x").next_to(axis,RIGHT)
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

        vector1 = Vector([0,0])
        vector1.add_updater(lambda mob: mob.become(Vector(vecField1(p1))).move_to(p1).shift(p1.get_center() - vector1.get_start()).set_color(YELLOW))

        self.play(Write(ihatvec),Write(ihat))
        self.play(Write(jhatvec),Write(jhat))
        self.play(Write(field_equation1_example1[2]))
        self.play(Write(vector1))

        


        # func1 = lambda pos: scalar*((pos[1]-1)*RIGHT + -pos[0]*UP)/(pos[0]**2+(pos[1]-1)**2+e) + scalar*((-(pos[1]+1))*RIGHT + pos[0]*UP)/(pos[0]**2+(-(pos[1]+1))**2+e)
        # stream = StreamLines(func1, stroke_width=2, max_anchors_per_line=300, virtual_time=50, n_repeats=5)
        # self.add(NumberPlane())
        # self.add(stream)
        # stream.start_animation(warm_up=False, flow_speed=2.5)
        # self.wait(5)


class GaussLaw(Scene):
    def construct(self):

        gausslaw = MathTex(r"\phi=\frac{q}{\varepsilon_{0}}")
        integral_form = MathTex(r"\oint_{A}E\cdot d\textbf{A}=\frac{q}{\varepsilon_{0}}")

        numberplane = NumberPlane().set_opacity(0.2)
        circle = Circle(radius=3.5, color=BLUE)
        arcphi = Arc()
        phi = MathTex(r"\varphi").set_color(YELLOW)
        phi2 = MathTex(r"\varphi").set_color(YELLOW)
        dphi = MathTex(r"d\varphi").set_color(YELLOW)
    
        r = MathTex(r"r").set_color(GREEN)
        r_line1 = Line(start=[0,0,0], end=[0,0,0])
        r_line2 = Line(start=[0,0,0], end=[0,0,0])
        point = Circle().set_opacity(0)

        phi_angle = ValueTracker(0)
        radius = ValueTracker(3.5)

        circle.add_updater(lambda mob: mob.become(Circle(radius=radius.get_value(), color=BLUE).move_to(point)))
        phi.add_updater(lambda mob: mob.move_to([2*np.cos(0.5*phi_angle.get_value()+PI/2) + circle.get_x(), 2*np.sin(0.5*phi_angle.get_value()+PI/2) + circle.get_y() ,0]))
        phi2.add_updater(lambda mob: mob.move_to([2*np.cos(0.5*phi_angle.get_value()+PI/2) + circle.get_x(), 2*np.sin(0.5*phi_angle.get_value()+PI/2) + circle.get_y() ,0]))
        dphi.add_updater(lambda mob: mob.move_to([2*np.cos(0.5*phi_angle.get_value()+PI/2) + circle.get_x(), 2*np.sin(0.5*phi_angle.get_value()+PI/2) + circle.get_y() ,0]))
        arcphi.add_updater(lambda mob: mob.become(Arc(radius=radius.get_value(), start_angle=PI/2, angle=phi_angle.get_value(), arc_center=circle.get_center(), color=YELLOW)))
        r_line1.add_updater(lambda mob: mob.become(Line(start=circle.get_center(), end=arcphi.get_end(), color=GREEN)))
        r_line2.add_updater(lambda mob: mob.become(Line(start=circle.get_center(), end=arcphi.get_start(), color=GREEN)))
        r.add_updater(lambda mob: mob.move_to(r_line1).shift(RIGHT*0.3+DOWN*0.3))

        dlphi = MathTex(r"dL_{\varphi}=r\cdot d\varphi ")
        dltheta = MathTex(r"dL_{\theta }=r\cdot sin(\varphi ) d\theta ")
        dlA1= MathTex(r"dA=dL_{\varphi} \cdot dL_{\theta }")
        dlA2= MathTex(r"dA=r\cdot d\varphi \cdot r\cdot sin(\varphi ) d\theta")
        dlA= MathTex(r"dA=r^{2}sin(\varphi )d\varphi d\theta ")

        self.add(numberplane, circle, arcphi, phi, r_line1, r_line2, r)
        self.play(phi_angle.animate.set_value(-PI/2))
        self.play(point.animate.shift(DOWN*3.5+LEFT*1), radius.animate.set_value(7))
        self.play(ReplacementTransform(phi,dphi))
        self.play(phi_angle.animate.set_value(-0.2))
        self.play(point.animate.shift(DOWN*97+LEFT*1), radius.animate.set_value(100), phi_angle.animate.set_value(-0.05))
        self.play(point.animate.shift(DOWN*800+LEFT*0), radius.animate.set_value(900), phi_angle.animate.set_value(-0.008))
        self.play(point.animate.shift(UP*897+LEFT*0), radius.animate.set_value(7), phi_angle.animate.set_value(-PI/4))
        self.wait()
        self.play(ReplacementTransform(dphi,phi2))

        self.play(phi_angle.animate.set_value(-PI/2), radius.animate.set_value(3.5), point.animate.shift(DOWN*-3.5+LEFT*-2))

        ellipse = Ellipse()
        ellipse.add_updater(lambda mob: mob.become(Ellipse(width=2*radius.get_value()*np.sin(phi_angle.get_value()), height=0.5*radius.get_value()*np.sin(phi_angle.get_value()), color=GREEN).move_to([0,arcphi.get_end()[1],0])))

        r2 = MathTex(r"r").set_color(YELLOW)
        r2_line1 = Line(start=[0,0,0], end=[0,0,0])
        r2_line1.add_updater(lambda mob: mob.become(Line(start=ellipse.get_center(), end=ellipse.get_right(), color=GREEN)))
        r2.add_updater(lambda mob: mob.next_to(r2_line1, DOWN))

        self.add(ellipse, r2, r2_line1)
        self.remove(r,r_line1,r_line2)
        self.play(phi_angle.animate.set_value(-PI/4))
        self.play(phi_angle.animate.set_value(-3*PI/4))
        self.play(phi_angle.animate.set_value(-PI/4))
        self.play(Write(dltheta))




















