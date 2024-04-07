package com.example.cafeteriaapp

import android.content.Context
import android.graphics.Canvas
import android.graphics.Paint
import android.util.AttributeSet
import android.view.View

class DrawingView(context: Context, attrs: AttributeSet?) : View(context) {


    private val paint = Paint();

    public override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)

        canvas.drawRect(200f,20f,240f,200f,paint);
        canvas.drawRect(20f,20f,200f,60f,paint);
        canvas.drawRect(20f,160f,200f,200f,paint);
        canvas.drawRect(90f,90f,200f,130f,paint);

        canvas.drawRect(200f,400f,240f,600f,paint);
        canvas.drawRect(20f,400f,60f,600f,paint);
        canvas.drawRect(20f,470f,200f,510f,paint);

        canvas.drawRect(200f,800f,240f,1000f,paint);
        canvas.drawRect(20f,800f,60f,1000f,paint);
        canvas.drawRect(20f,870f,200f,910f,paint);

        canvas.drawRect(20f,870f,200f,910f,paint);

        canvas.drawRect(200f,800f,240f,1000f,paint);
        canvas.drawRect(20f,1200f,60f,1300f,paint);

        canvas.drawRect(20f,800f,60f,1000f,paint);
        canvas.drawRect(20f,20f,200f,60f,paint);
        canvas.drawRect(20f,1200f,240f,1240f,paint);
        canvas.drawRect(90f,90f,200f,130f,paint);
        canvas.drawRect(20f,470f,200f,510f,paint);
        canvas.drawRect(200f,400f,240f,600f,paint);
        canvas.drawRect(200f,20f,240f,200f,paint);
        canvas.drawRect(20f,400f,60f,600f,paint);
        canvas.drawRect(20f,160f,200f,200f,paint);
        canvas.drawRect(20f,470f,200f,510f,paint);
        canvas.drawRect(20f,20f,200f,60f,paint);

        canvas.drawRect(20f,400f,60f,600f,paint);
        canvas.drawRect(20f,1200f,60f,1300f,paint);

        canvas.drawRect(90f,90f,200f,130f,paint);
        canvas.drawRect(20f,160f,200f,200f,paint);
        canvas.drawRect(20f,870f,200f,910f,paint);
        canvas.drawRect(200f,20f,240f,200f,paint);
        canvas.drawRect(20f,1200f,240f,1240f,paint);
        canvas.drawRect(20f,800f,60f,1000f,paint);
        canvas.drawRect(200f,800f,240f,1000f,paint);
        canvas.drawRect(20f,160f,200f,200f,paint);
        canvas.drawRect(20f,20f,200f,60f,paint);
        canvas.drawRect(200f,400f,240f,600f,paint);
        canvas.drawRect(20f,800f,60f,1000f,paint);
        canvas.drawRect(90f,90f,200f,130f,paint);
        canvas.drawRect(20f,470f,200f,510f,paint);
        canvas.drawRect(20f,400f,60f,600f,paint);

        canvas.drawRect(20f,1200f,240f,1240f,paint);
        canvas.drawRect(200f,20f,240f,200f,paint);
        canvas.drawRect(20f,1200f,60f,1300f,paint);
        canvas.drawRect(20f,870f,200f,910f,paint);


        canvas.drawRect(200f,800f,240f,1000f,paint);
        canvas.drawRect(200f,400f,240f,600f,paint);
        canvas.drawRect(20f,1200f,60f,1300f,paint);
        canvas.drawRect(20f,1200f,240f,1240f,paint);
        paint.strokeWidth = 40f;
        canvas.drawLine(235f,1200f,40f,1600f, paint);
    }
}