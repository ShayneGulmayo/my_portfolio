package com.labactivity.simregistrationapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.labactivity.simregistrationapp.databinding.ActivityMain2Binding
import com.labactivity.simregistrationapp.databinding.ActivityMainBinding

class MainActivity2 : AppCompatActivity() {
    private lateinit var binding: ActivityMain2Binding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMain2Binding.inflate(layoutInflater)
        setContentView(binding.root)

        val name = intent.getStringExtra("nameData")
        val contactNo = intent.getStringExtra("contactNoData")
        val simNetwork = intent.getStringExtra("simNetworkData")
        val address = intent.getStringExtra("addressData")

        binding.editTxtDetails.append("$name\n\n")
        binding.editTxtDetails.append("$contactNo\n\n")
        binding.editTxtDetails.append("$simNetwork\n\n")
        binding.editTxtDetails.append("$address")


    }
}