package com.labactivity.studybuddy

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.database.ValueEventListener
import com.labactivity.studybuddy.databinding.ActivityMainBinding
import java.util.UUID

class MainActivity : AppCompatActivity() {
    private lateinit var dbref: DatabaseReference
    private lateinit var adapter: AdapterClass
    private lateinit var cardArray: ArrayList<DataClass>
    private lateinit var binding:ActivityMainBinding
    private var cardNo:String = UUID.randomUUID().toString()
    private var clickedCardNo:String =""
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.recyclerView.layoutManager = LinearLayoutManager(this)

        cardArray = arrayListOf<DataClass>()
        getCard()
        adapter = AdapterClass(cardArray) {
                clickedItem ->
            val intent = Intent(this, flview::class.java)
            intent.putExtra("question", clickedItem.question)
            intent.putExtra("answer", clickedItem.answer)
            val parentRef: DatabaseReference = FirebaseDatabase.getInstance().getReference("Users/admin/cards")
            parentRef.addListenerForSingleValueEvent(object : ValueEventListener {
                override fun onDataChange(dataSnapshot: DataSnapshot) {
                    for (childSnapshot in dataSnapshot.children) {
                        for (grandChildSnapshot in childSnapshot.children) {
                            if (grandChildSnapshot.value == clickedItem.question) {
                                clickedCardNo = childSnapshot.key ?: ""
                                intent.putExtra("cardNo", clickedCardNo)
                                startActivity(intent)
                                return
                            }
                        }
                    }
                }

                override fun onCancelled(databaseError: DatabaseError) {
                    // Handle error
                }
            })

        }

        binding.recyclerView.adapter = adapter




        binding.imgBtnAdd.setOnClickListener() {
            val intent = Intent(this, inputQuestions::class.java)
            intent.putExtra("cardNo", cardNo)
            startActivity(intent)
        }

        binding.imgBtnUser.setOnClickListener() {
            val intent = Intent(this, userProfile::class.java)
            startActivity(intent)
        }

    }

    private fun getCard() {

        dbref = FirebaseDatabase.getInstance().getReference("Users/admin/cards")
        dbref.addValueEventListener(object: ValueEventListener{
            override fun onDataChange(snapshot: DataSnapshot) {

                if (snapshot.exists()){
                    cardArray.clear()
                    for (cardSnapshot in snapshot.children){
                        val cards = cardSnapshot.getValue(DataClass::class.java)
                        cardArray.add(cards!!)
                    }
                    adapter.notifyDataSetChanged()
                }

            }

            override fun onCancelled(error: DatabaseError) {
                TODO("Not yet implemented")
            }

        })

    }
}