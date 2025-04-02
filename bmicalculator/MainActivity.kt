package com.labactivity.bmicalculator

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.labactivity.bmicalculator.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)


            binding.btnCompute.setOnClickListener() {
                var fname: String = binding.txtName.text.toString()
                var mi: String = binding.txtMI.text.toString()
                var lname: String = binding.txtLname.text.toString()
                var gender: String = if (binding.radBtnMale.isChecked) "MR." else "MS."
                var height: Double = binding.txtHeight.text.toString().toDouble()
                var weight: Double = binding.txtWeight.text.toString().toDouble()


                val intent = Intent(this, MainActivity2::class.java)
                intent.putExtra("fname", fname)
                intent.putExtra("mi", mi)
                intent.putExtra("lname", lname)
                intent.putExtra("gender", gender)
                intent.putExtra("height", height)
                intent.putExtra("weight", weight)
                startActivity(intent)

            }
        }
    }