package com.labactivity.recipekeeper

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.labactivity.recipekeeper.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        var recipe: String = ""
        var ingredients: String = ""
        var instructions: String = ""

        binding.btnAddRecipe.setOnClickListener() {
            recipe = binding.edtRecipeName.text.toString()
            binding.edtRecipeArea.append("$recipe\n")
        }
        binding.btnAddIngredients.setOnClickListener() {
            ingredients = binding.edtIngredients.text.toString()
            binding.edtRecipeArea.append("\nIngredients:\n$ingredients\n")
        }
        binding.btnAddInstructions.setOnClickListener() {
            instructions = binding.edtInstructions.text.toString()
            binding.edtRecipeArea.append("\nInstructions:\n$instructions\n")
        }

        binding.btnSaveRecipe.setOnClickListener() {
            if (recipe.isNotEmpty() || ingredients.isNotEmpty() || instructions.isNotEmpty()) {
                Toast.makeText(applicationContext, "Recipe Saved", Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(applicationContext, "Please complete all required information", Toast.LENGTH_SHORT).show()
            }
        }

        binding.btnClear.setOnClickListener() {
            binding.edtRecipeName.text.clear()
            binding.edtIngredients.text.clear()
            binding.edtInstructions.text.clear()
            binding.edtRecipeArea.text.clear()
            recipe = ""
            ingredients = ""
            instructions = ""
        }
    }
}