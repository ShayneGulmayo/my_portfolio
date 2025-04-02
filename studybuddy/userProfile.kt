package com.labactivity.studybuddy

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.FirebaseDatabase
import com.labactivity.studybuddy.databinding.ActivityUserProfileBinding

class userProfile : AppCompatActivity() {
    private lateinit var binding:ActivityUserProfileBinding
    private lateinit var database:DatabaseReference
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding=ActivityUserProfileBinding.inflate(layoutInflater)
        setContentView(binding.root)

        getInfo()

        binding.imgBtnHome.setOnClickListener() {
            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
        }
        binding.btnLogout.setOnClickListener() {
            val intent = Intent(this, login::class.java)
            startActivity(intent)
        }

    }

    private fun getInfo() {
        database = FirebaseDatabase.getInstance().getReference("Users")
        database.child("admin").get().addOnSuccessListener {
            if (it.exists()){

                val name = it.child("name").getValue(String::class.java)
                val username = it.child("username").getValue(String::class.java)

                binding.txtName.text = name.toString()
                binding.txtUsername.text = username.toString()

            }
        }
    }
}