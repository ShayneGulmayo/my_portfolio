package com.labactivity.lyricsviewerapplication

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.labactivity.lyricsviewerapplication.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnSong3.setOnClickListener(){
            val intent = Intent(this,MainActivity2::class.java)
            startActivity(intent)
        }

        binding.btnSong4.setOnClickListener(){
            val intent = Intent(this,MainActivity3::class.java)
            startActivity(intent)
        }

        binding.btnSong5.setOnClickListener(){
            val intent = Intent(this,MainActivity4::class.java)
            startActivity(intent)
        }

        binding.btnSong1.setOnClickListener(){
            val intent = Intent(this,MainActivity5::class.java)
            startActivity(intent)
        }

        binding.btnSong2.setOnClickListener(){
            val intent = Intent(this,MainActivity6::class.java)
            startActivity(intent)
        }

    }
}