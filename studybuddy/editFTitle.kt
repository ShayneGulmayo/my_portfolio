package com.labactivity.studybuddy

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.labactivity.studybuddy.databinding.ActivityEditFtitleBinding

class editFTitle : AppCompatActivity() {
    private lateinit var binding:ActivityEditFtitleBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding=ActivityEditFtitleBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnSave.setOnClickListener() {
            val intent = Intent(this, MainActivity::class.java)
            val title:String = binding.edtTxtEnterFl.text.toString()
            intent.putExtra("title",title)
            startActivity(intent)
        }

        binding.imgBtnUser.setOnClickListener() {
            val intent = Intent(this, userProfile::class.java)
            startActivity(intent)
        }
        binding.imgBtnHome.setOnClickListener() {
            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
        }
    }
}