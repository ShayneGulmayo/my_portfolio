package com.labactivity.studybuddy

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.google.firebase.database.DatabaseReference
import com.labactivity.studybuddy.databinding.ActivityLoginBinding

class login : AppCompatActivity() {
    private lateinit var binding:ActivityLoginBinding
    private lateinit var db:DatabaseReference
    private val defaultUsername = "admin"
    private val defaultPassword = "admin123"
    private var enteredUsername = ""
    private var enteredPassword = ""
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding=ActivityLoginBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnLogin.setOnClickListener(){
            enteredUsername = binding.edtTxtUsername.text.toString()
            enteredPassword = binding.edtTxtPassword.text.toString()

            if(enteredUsername.isEmpty()){
                Toast.makeText(applicationContext,"Enter Username", Toast.LENGTH_SHORT).show()
            }
            else if(enteredPassword.isEmpty()) {
                Toast.makeText(applicationContext, "Enter Password", Toast.LENGTH_SHORT).show()
            }
            else if(enteredUsername == defaultUsername && enteredPassword == defaultPassword){
                val intent = Intent(this, MainActivity::class.java)
                Toast.makeText(applicationContext,"Logging in...", Toast.LENGTH_SHORT).show()
                startActivity(intent)
            }
            else{
                Toast.makeText(applicationContext,"Invalid Username or Password", Toast.LENGTH_SHORT).show()
            } 
        }
    }
}