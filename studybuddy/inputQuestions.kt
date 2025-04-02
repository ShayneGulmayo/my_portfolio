package com.labactivity.studybuddy

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.FirebaseDatabase
import com.labactivity.studybuddy.databinding.ActivityInputQuestionsBinding

class inputQuestions : AppCompatActivity() {
    private lateinit var binding:ActivityInputQuestionsBinding
    private lateinit var dbref:DatabaseReference
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding=ActivityInputQuestionsBinding.inflate(layoutInflater)
        setContentView(binding.root)

        dbref = FirebaseDatabase.getInstance().getReference("Users/admin/cards")
        val cardNo = intent.getStringExtra("cardNo")
        binding.btnSaveCard.setOnClickListener() {
            val intent = Intent(this, MainActivity::class.java)
            val question:String = binding.edtTxtQuestion.text.toString()
            val answer:String = binding.edtTxtAnswer.text.toString()
            if(question.isNotEmpty()&&answer.isNotEmpty()) {
                val dataclass = DataClass(question, answer)
                if (cardNo != null) {
                    dbref.child(cardNo).setValue(dataclass).addOnCompleteListener {
                        if (it.isSuccessful) {
                            Toast.makeText(this, "Successfully added cards", Toast.LENGTH_SHORT).show()
                        } else {
                            Toast.makeText(this, "Failed to add cards", Toast.LENGTH_SHORT).show()
                        }
                    }
                }
                startActivity(intent)
                finish()
            }else{
                Toast.makeText(this, "Please complete the fields", Toast.LENGTH_SHORT).show()
            }

        }
        binding.btnDiscardCard.setOnClickListener{
            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
            finish()
        }

        binding.imgBtnUser.setOnClickListener() {
            val intent = Intent(this, userProfile::class.java)
            startActivity(intent)
            finish()
        }

        binding.imgBtnHome.setOnClickListener() {
            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
            finish()
        }

    }
}