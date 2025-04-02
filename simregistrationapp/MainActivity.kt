package com.labactivity.simregistrationapp

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.labactivity.simregistrationapp.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnRegister.setOnClickListener() {
            val intent= Intent(this,MainActivity2::class.java)
            var name:String =  binding.editTxtName.text.toString()
            var contactNo:String = binding.editTxtNo.text.toString()
            var simNetwork:String = binding.editTxtSim.text.toString()
            var address:String = binding.editTxtAddress.text.toString()

            intent.putExtra("nameData",name)
            intent.putExtra("contactNoData",contactNo)
            intent.putExtra("simNetworkData",simNetwork)
            intent.putExtra("addressData",address)
            startActivity(intent)
        }

    }
}