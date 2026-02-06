
import React from 'react';
import { SafeAreaView, Text, View } from 'react-native';

export default function App(){
  return (
    <SafeAreaView style={{flex:1, backgroundColor:'#05070f'}}>
      <View style={{padding:20}}>
        <Text style={{color:'#00ffe0', fontSize:28, fontWeight:'800'}}>NOETIVIS</Text>
        <Text style={{color:'#e6fff9', marginTop:8}}>Mobile Intelligence Console</Text>
      </View>
    </SafeAreaView>
  );
}
