package com.labactivity.studybuddy

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.labactivity.studybuddy.databinding.CardviewFlashcardsBinding

class AdapterClass(val card:ArrayList<DataClass>, val onItemClick: (DataClass) -> Unit):RecyclerView.Adapter<AdapterClass.ViewHolder>(){
    class ViewHolder(val binding: CardviewFlashcardsBinding):RecyclerView.ViewHolder(binding.root){
        val question = binding.txtFQuestion
        val answer = binding.txtFAnswer

    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): AdapterClass.ViewHolder {
        return ViewHolder(CardviewFlashcardsBinding.inflate(LayoutInflater.from(parent.context),parent, false))
    }

    override fun onBindViewHolder(holder: AdapterClass.ViewHolder, position: Int) {
        val card = card[position]
        holder.question.text = card.question
        holder.answer.text = card.answer

        holder.itemView.setOnClickListener{
            onItemClick(card)
        }

    }
    override fun getItemCount(): Int {
        return card.size
    }



}