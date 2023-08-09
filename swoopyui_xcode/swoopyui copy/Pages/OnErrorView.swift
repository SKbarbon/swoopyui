//
//  OnErrorView.swift
//  swoopyui
//
//  Created by Yousif Aladwani on 18/05/2023.
//

import SwiftUI

struct OnErrorView: View {
    @State var error = "This is error!"
    var body: some View {
        VStack {
            Image(systemName: "info.circle.fill")
                .resizable()
                .scaledToFit()
                .frame(width: 25)
                .foregroundColor(.red)
            Text("\(error)")
                .font(.system(size: 18))
        }
    }
}

struct OnErrorView_Previews: PreviewProvider {
    static var previews: some View {
        OnErrorView()
    }
}
