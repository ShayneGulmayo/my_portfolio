package com.labactivity.studybuddy

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.FirebaseDatabase
import com.labactivity.studybuddy.databinding.ActivityFlviewBinding

class flview : AppCompatActivity() {
    private lateinit var binding:ActivityFlviewBinding
    private lateinit var dbref:DatabaseReference
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding=ActivityFlviewBinding.inflate(layoutInflater)
        setContentView(binding.root)

        dbref = FirebaseDatabase.getInstance().getReference("Users/admin/cards")

        val q = intent.getStringExtra("question")
        val a = intent.getStringExtra("answer")
        val cardNo = intent.getStringExtra("cardNo").toString()


        binding.txtDisplayQues.text = q
        binding.txtDisplayAns.text = a

        binding.btnShowAnswer.setOnClickListener{
            binding.txtDisplayAns.visibility = android.view.View.VISIBLE
        }

        binding.btnDelete.setOnClickListener{
            dbref.child(cardNo).removeValue().addOnSuccessListener {
                Toast.makeText(this, "Card deleted successfully", Toast.LENGTH_SHORT).show()
                finish()
            }.addOnFailureListener { exception ->
                Toast.makeText(this, "Failed to delete card: ${exception.message}", Toast.LENGTH_SHORT).show()
            }
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