package com.labactivity.bmicalculator

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.core.content.ContextCompat
import com.labactivity.bmicalculator.databinding.ActivityMain2Binding

class MainActivity2 : AppCompatActivity() {
    private lateinit var binding: ActivityMain2Binding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMain2Binding.inflate(layoutInflater)
        setContentView(binding.root)

        val fname = intent.getStringExtra("fname")
        val mi = intent.getStringExtra("mi")
        val lname = intent.getStringExtra("lname")
        val gender = intent.getStringExtra("gender")
        val height:Double = intent.getDoubleExtra("height", 0.0)
        val weight:Double = intent.getDoubleExtra("weight", 0.0)

        var fullName = "$fname $mi $lname"
        binding.txtGender.text = gender
        binding.txtFullName.text = fullName

        var calHeight = height/100
        var bmi = weight / (calHeight * calHeight)

        binding.txtBMI.text = String.format("%.2f", bmi)


        when{
            (bmi < 18.5) -> {
                binding.txtStatus.text = "UNDERWEIGHT"
                binding.txtStatus.setTextColor(ContextCompat.getColor(this, R.color.red))
                binding.txtCond1.setBackgroundColor(ContextCompat.getColor(this, R.color.red))
            }
            (bmi>=18.5 &&bmi<25.0) -> {
                binding.txtStatus.text = "HEALTHY WEIGHT"
                binding.txtStatus.setTextColor(ContextCompat.getColor(this, R.color.green))
                binding.txtCond2.setBackgroundColor(ContextCompat.getColor(this, R.color.green))
            }
            (bmi>=25.0&&bmi<30.0) -> {
                binding.txtStatus.text = "OVERWEIGHT"
                binding.txtStatus.setTextColor(ContextCompat.getColor(this, R.color.red))
                binding.txtCond3.setBackgroundColor(ContextCompat.getColor(this, R.color.red))
            }
            (bmi > 30.0)-> {
                binding.txtStatus.text = "OBESE"
                binding.txtStatus.setTextColor(ContextCompat.getColor(this, R.color.red))
                binding.txtCond4.setBackgroundColor(ContextCompat.getColor(this, R.color.red))
            }
        }











    }
}